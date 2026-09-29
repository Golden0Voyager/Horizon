"""Layer 1 (non-Playwright) unit tests for ``src.scrapers.twitter_playwright``.

``TwitterPlaywrightScraper`` is the ``twitter.mode == "playwright"`` parallel
implementation of the cookie-based GraphQL scraper. Like
``tests/test_twitter_scraper_unit.py`` (which covers ``src.scrapers.twitter``),
these tests exercise the pure helpers (``_get_proxy``, ``_load_browser_cookies``,
``_parse_tweet``), the ``fetch`` early-return branches, and drive
``_scrape_user`` with the shared fake page/context fakes — no real chromium,
no network, and the 60-second polling loop is short-circuited via patched
clocks.

The fakes and payload helpers are imported from
``test_twitter_scraper_unit`` (the two modules share the same fake surface);
the only scraper-specific pieces live here: the clock patch target
(``src.scrapers.twitter_playwright``) and the ``TwitterPlaywrightScraper``
driver.
"""

from __future__ import annotations

import asyncio
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pytest
from test_twitter_scraper_unit import (
    _FakeContext,
    _FakePage,
    _make_tweet_payload,
    _wrap_tweet_envelope,
    _yield_n,
)

from src.models import TwitterConfig
from src.scrapers.twitter_playwright import (
    TwitterPlaywrightScraper,
    _get_proxy,
    _load_browser_cookies,
)

_LOGGER = "src.scrapers.twitter_playwright"


# ---------------------------------------------------------------------------
# _get_proxy
# ---------------------------------------------------------------------------


def test_get_proxy_returns_first_set_env_var(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("PROXY", raising=False)
    monkeypatch.delenv("https_proxy", raising=False)
    monkeypatch.delenv("http_proxy", raising=False)
    monkeypatch.delenv("all_proxy", raising=False)
    assert _get_proxy() == ""


def test_get_proxy_prefers_pro_and_falls_through(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # PROXY wins when set.
    monkeypatch.setenv("PROXY", "http://proxy:3128")
    monkeypatch.setenv("https_proxy", "http://other:3128")
    assert _get_proxy() == "http://proxy:3128"

    # With PROXY empty/whitespace, fall through to https_proxy.
    monkeypatch.setenv("PROXY", "   ")
    assert _get_proxy() == "http://other:3128"

    # Whitespace-only values are stripped and treated as unset.
    monkeypatch.setenv("https_proxy", "")
    monkeypatch.setenv("http_proxy", "http://http-proxy:8080")
    assert _get_proxy() == "http://http-proxy:8080"

    monkeypatch.setenv("http_proxy", "")
    monkeypatch.setenv("all_proxy", "socks5://tunnel:1080")
    assert _get_proxy() == "socks5://tunnel:1080"


# ---------------------------------------------------------------------------
# _load_browser_cookies
# ---------------------------------------------------------------------------


def test_pw_load_browser_cookies_returns_empty_when_file_missing(tmp_path: Path) -> None:
    assert _load_browser_cookies(str(tmp_path / "missing.json")) == []


def test_pw_load_browser_cookies_converts_to_playwright_format(tmp_path: Path) -> None:
    fixture = [
        {
            "name": "auth_token",
            "value": "abc123",
            "domain": ".x.com",
            "path": "/",
            "secure": True,
            "httpOnly": True,
            "expirationDate": 1750000000.0,
        },
        {
            # optional fields absent → defaults (secure=True, httpOnly=False, path="/")
            "name": "ct0",
            "value": "def456",
            "domain": ".x.com",
        },
    ]
    path = tmp_path / "cookies.json"
    path.write_text(json.dumps(fixture), encoding="utf-8")

    out = _load_browser_cookies(str(path))
    assert len(out) == 2
    assert out[0]["name"] == "auth_token"
    assert "expires" in out[0]
    assert out[0]["expires"] == 1750000000.0
    assert "expires" not in out[1]
    assert out[1]["httpOnly"] is False
    assert out[1]["path"] == "/"


# ---------------------------------------------------------------------------
# _parse_tweet
# ---------------------------------------------------------------------------


def _pw_build_tweet_dict(**overrides: Any) -> dict[str, Any]:
    base = {
        "tweet_id": "1737000000000000000",
        "text": "hello world",
        "datetime_raw": "Wed Jan 15 12:00:00 +0000 2026",
        "is_retweet": False,
        "images": [],
    }
    base.update(overrides)
    base["datetime"] = datetime.strptime(base["datetime_raw"], "%a %b %d %H:%M:%S %z %Y").isoformat()
    return base


def _make_pw_scraper() -> TwitterPlaywrightScraper:
    return TwitterPlaywrightScraper(TwitterConfig())


def test_pw_parse_tweet_returns_content_item() -> None:
    tweet = _pw_build_tweet_dict(text="hello world this is a great tweet")
    item = _make_pw_scraper()._parse_tweet(tweet, "alice")
    assert item is not None
    assert "alice" in (item.author or "")
    assert item.title.startswith("@alice: hello world")
    assert item.url.host == "x.com"


def test_pw_parse_tweet_returns_none_when_tweet_id_missing() -> None:
    tweet = _pw_build_tweet_dict()
    tweet["tweet_id"] = ""
    assert _make_pw_scraper()._parse_tweet(tweet, "alice") is None


def test_pw_parse_tweet_returns_none_when_text_empty() -> None:
    tweet = _pw_build_tweet_dict(text="")
    assert _make_pw_scraper()._parse_tweet(tweet, "alice") is None


def test_pw_parse_tweet_returns_none_when_unparseable_datetime() -> None:
    # Production reads ``tweet["datetime"]`` (not ``datetime_raw``).
    tweet = _pw_build_tweet_dict()
    tweet["datetime"] = "not-an-iso-timestamp"
    assert _make_pw_scraper()._parse_tweet(tweet, "alice") is None


def test_pw_parse_tweet_naive_datetime_becomes_utc() -> None:
    tweet = _pw_build_tweet_dict()
    tweet["datetime"] = "2026-01-15T12:00:00"  # tz-naive → tzinfo is None branch
    item = _make_pw_scraper()._parse_tweet(tweet, "alice")
    assert item is not None
    assert item.published_at is not None
    assert item.published_at.utcoffset() is not None
    assert item.published_at.utcoffset().total_seconds() == 0


def test_pw_parse_tweet_truncates_long_title_to_50_chars_with_ellipsis() -> None:
    tweet = _pw_build_tweet_dict(text="x" * 80)
    item = _make_pw_scraper()._parse_tweet(tweet, "alice")
    assert item is not None
    title_body = item.title.replace("@alice: ", "")
    assert title_body.endswith("...")
    assert len(title_body) <= 60


def test_pw_parse_tweet_includes_images_in_metadata() -> None:
    images = [
        "https://pbs.twimg.com/media/aaa.jpg",
        "https://pbs.twimg.com/media/bbb.jpg",
    ]
    tweet = _pw_build_tweet_dict(images=images)
    item = _make_pw_scraper()._parse_tweet(tweet, "alice")
    assert item is not None
    assert item.metadata["images"] == images


# ---------------------------------------------------------------------------
# fetch (early-return branches)
# ---------------------------------------------------------------------------


def test_pw_fetch_returns_empty_when_config_disabled() -> None:
    cfg = TwitterConfig(enabled=False, users=["alice"])
    scraper = TwitterPlaywrightScraper(cfg)
    out = asyncio.run(scraper.fetch(datetime(2026, 1, 1, tzinfo=UTC)))
    assert out == []


def test_pw_fetch_returns_empty_when_no_users() -> None:
    cfg = TwitterConfig(enabled=True, users=[])
    scraper = TwitterPlaywrightScraper(cfg)
    out = asyncio.run(scraper.fetch(datetime(2026, 1, 1, tzinfo=UTC)))
    assert out == []


def test_pw_fetch_returns_empty_when_no_playwright(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("src.scrapers.twitter_playwright.PLAYWRIGHT_AVAILABLE", False)
    cfg = TwitterConfig(enabled=True, users=["alice"])
    scraper = TwitterPlaywrightScraper(cfg)
    out = asyncio.run(scraper.fetch(datetime(2026, 1, 1, tzinfo=UTC)))
    assert out == []


def test_pw_fetch_returns_empty_when_no_cookie_files(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Force past the Playwright gate so the cookie-directory check is reached,
    # then point at an empty dir → returns [] before any browser is launched.
    monkeypatch.setattr("src.scrapers.twitter_playwright.PLAYWRIGHT_AVAILABLE", True)
    cfg = TwitterConfig(
        enabled=True,
        users=["alice"],
        cookie_dir=str(tmp_path / "no_cookies"),
        cookie_file_pattern="x_cookies_*.json",
    )
    scraper = TwitterPlaywrightScraper(cfg)
    out = asyncio.run(scraper.fetch(datetime(2026, 1, 1, tzinfo=UTC)))
    assert out == []


# ---------------------------------------------------------------------------
# _scrape_user (fake page/context, patched clocks)
# ---------------------------------------------------------------------------


@pytest.fixture
def _patch_pw_scrape_clocks(monkeypatch: pytest.MonkeyPatch) -> None:
    """Make ``_scrape_user`` finish in milliseconds instead of 60 seconds.

    Mirrors ``test_twitter_scraper_unit._patch_scrape_clocks`` but targets
    ``src.scrapers.twitter_playwright``:

    - ``asyncio.sleep`` becomes a no-op that still yields to the running loop
      (so the test runner's ``_yield_n`` tick loop keeps advancing the
      scheduled task).
    - ``asyncio.get_event_loop`` returns a fake whose ``time()`` is pinned at
      ``0.0`` so the ``while (…) < 60`` bound never trips; the loop exits
      naturally via the ``return result`` branch once a dispatched response
      populates the captured ``graphql_tweets`` list.
    """

    async def _no_sleep_yield(*_a: Any, **_kw: Any) -> None:
        try:
            running = asyncio.get_running_loop()
        except RuntimeError:
            return
        fut = running.create_future()
        running.call_soon(fut.set_result, None)
        await fut

    monkeypatch.setattr("src.scrapers.twitter_playwright.asyncio.sleep", _no_sleep_yield)

    class _FakeLoop:
        def time(self) -> float:
            return 0.0

    monkeypatch.setattr(
        "src.scrapers.twitter_playwright.asyncio.get_event_loop",
        lambda: _FakeLoop(),
    )


def _advance_clock_fixture(
    monkeypatch: pytest.MonkeyPatch,
    step: float = 30.0,
) -> None:
    """Pin ``time()`` to advance by ``step`` seconds per call so the polling
    loop's ``while (…) < 60`` bound trips within a couple of iterations. Used by
    the no-dispatch / error-page / at-bottom paths that must exit the loop
    WITHOUT a GraphQL payload.
    """
    _n = [0]

    class _AdvancingLoop:
        def time(self) -> float:
            _n[0] += 1
            return (_n[0] - 1) * step

    monkeypatch.setattr(
        "src.scrapers.twitter_playwright.asyncio.get_event_loop",
        lambda: _AdvancingLoop(),
    )


def _drive_pw_scrape_user(
    tweets: list[dict[str, Any]],
    since: datetime,
    *,
    fetch_limit: int = 10,
    username: str = "alice",
) -> list[dict[str, Any]] | None:
    """Synchronously drive ``_scrape_user`` + dispatch canned GraphQL mid-flight."""
    page = _FakePage()
    ctx = _FakeContext(page)
    cfg = TwitterConfig(fetch_limit=fetch_limit)
    scraper = TwitterPlaywrightScraper(cfg)
    envelopes = [_wrap_tweet_envelope(t) for t in tweets]

    async def _runner() -> list[dict[str, Any]] | None:
        task = asyncio.create_task(scraper._scrape_user(ctx, username, since))
        await _yield_n(50)
        for env in envelopes:
            await page.dispatch(
                "https://x.com/i/api/graphql/x/UserTweets?variables=foo",
                env,
            )
        return await task

    return asyncio.run(_runner())


def test_pw_scrape_user_returns_tweets_when_graphql_match(
    _patch_pw_scrape_clocks: None,
) -> None:
    since = datetime(2026, 1, 1, tzinfo=UTC)
    out = _drive_pw_scrape_user(
        [
            _make_tweet_payload(
                tweet_id="1001",
                text="hello world",
                created_at="Fri Jan 02 12:00:00 +0000 2026",
            ),
        ],
        since,
    )
    assert out is not None
    assert len(out) == 1
    assert out[0]["tweet_id"] == "1001"
    assert out[0]["text"] == "hello world"


def test_pw_scrape_user_skips_tweets_outside_time_window(
    _patch_pw_scrape_clocks: None,
) -> None:
    since = datetime(2026, 1, 5, tzinfo=UTC)
    out = _drive_pw_scrape_user(
        [
            _make_tweet_payload(
                tweet_id="OLD",
                text="old tweet",
                created_at="Thu Jan 01 12:00:00 +0000 2026",
            ),
            _make_tweet_payload(
                tweet_id="NEW",
                text="new tweet",
                created_at="Sat Jan 10 12:00:00 +0000 2026",
            ),
        ],
        since,
    )
    assert out is not None
    assert len(out) == 1
    assert out[0]["tweet_id"] == "NEW"


def test_pw_scrape_user_extracts_images_from_extended_entities(
    _patch_pw_scrape_clocks: None,
) -> None:
    since = datetime(2026, 1, 1, tzinfo=UTC)
    out = _drive_pw_scrape_user(
        [
            _make_tweet_payload(
                tweet_id="1001",
                text="photo tweet",
                created_at="Fri Jan 02 12:00:00 +0000 2026",
                extended_media=[
                    "https://pbs.twimg.com/media/aaa.jpg",
                    "https://pbs.twimg.com/media/bbb.jpg",
                ],
            ),
        ],
        since,
    )
    assert out is not None
    assert out[0]["images"] == [
        "https://pbs.twimg.com/media/aaa.jpg",
        "https://pbs.twimg.com/media/bbb.jpg",
    ]


def test_pw_scrape_user_extracts_images_from_entities_fallback(
    _patch_pw_scrape_clocks: None,
) -> None:
    since = datetime(2026, 1, 1, tzinfo=UTC)
    out = _drive_pw_scrape_user(
        [
            _make_tweet_payload(
                tweet_id="1001",
                text="fallback photo",
                created_at="Fri Jan 02 12:00:00 +0000 2026",
                fallback_media=["https://pbs.twimg.com/media/ccc.jpg"],
            ),
        ],
        since,
    )
    assert out is not None
    assert out[0]["images"] == ["https://pbs.twimg.com/media/ccc.jpg"]


def test_pw_scrape_user_detects_retweet_via_core(_patch_pw_scrape_clocks: None) -> None:
    since = datetime(2026, 1, 1, tzinfo=UTC)
    out = _drive_pw_scrape_user(
        [
            _make_tweet_payload(
                tweet_id="1001",
                text="RT something",
                created_at="Fri Jan 02 12:00:00 +0000 2026",
                retweet_via="core",
            ),
        ],
        since,
    )
    assert out is not None
    assert out[0]["is_retweet"] is True


def test_pw_scrape_user_detects_retweet_via_legacy(_patch_pw_scrape_clocks: None) -> None:
    since = datetime(2026, 1, 1, tzinfo=UTC)
    out = _drive_pw_scrape_user(
        [
            _make_tweet_payload(
                tweet_id="1001",
                text="RT legacy",
                created_at="Fri Jan 02 12:00:00 +0000 2026",
                retweet_via="legacy",
            ),
        ],
        since,
    )
    assert out is not None
    assert out[0]["is_retweet"] is True


def test_pw_scrape_user_dedupes_by_tweet_id(_patch_pw_scrape_clocks: None) -> None:
    since = datetime(2026, 1, 1, tzinfo=UTC)
    payload = _make_tweet_payload(
        tweet_id="DUPE",
        text="dup",
        created_at="Fri Jan 02 12:00:00 +0000 2026",
    )
    out = _drive_pw_scrape_user([payload, payload], since)
    assert out is not None
    assert len(out) == 1
    assert out[0]["tweet_id"] == "DUPE"


def test_pw_scrape_user_truncates_to_fetch_limit(_patch_pw_scrape_clocks: None) -> None:
    since = datetime(2026, 1, 1, tzinfo=UTC)
    out = _drive_pw_scrape_user(
        [
            _make_tweet_payload(
                tweet_id=f"1{i}",
                text=f"tweet {i}",
                created_at="Fri Jan 02 12:00:00 +0000 2026",
            )
            for i in range(5)
        ],
        since,
        fetch_limit=3,
    )
    assert out is not None
    assert len(out) == 3


def test_pw_scrape_user_returns_empty_when_all_outside_window(
    _patch_pw_scrape_clocks: None,
) -> None:
    """All dispatched tweets are before ``since`` → time-window filter strips
    every entry → production returns ``[]`` (NOT ``None``)."""
    since = datetime(2026, 6, 1, tzinfo=UTC)  # late cutoff
    out = _drive_pw_scrape_user(
        [
            _make_tweet_payload(
                tweet_id="OLD1",
                text="oldest",
                created_at="Thu Jan 01 12:00:00 +0000 2026",
            ),
            _make_tweet_payload(
                tweet_id="OLD2",
                text="second-oldest",
                created_at="Fri Jan 02 12:00:00 +0000 2026",
            ),
        ],
        since,
    )
    assert out == []
    assert out is not None


def test_pw_scrape_user_logs_login_gate(
    _patch_pw_scrape_clocks: None,
    monkeypatch: pytest.MonkeyPatch,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """No GraphQL dispatched + login-gate body text → loop exits via the
    time bound → post-loop ``if not graphql_tweets: return None`` fires."""
    page = _FakePage()
    page.evaluate_return = "Please log in to continue"
    ctx = _FakeContext(page)
    cfg = TwitterConfig()
    scraper = TwitterPlaywrightScraper(cfg)
    since = datetime(2026, 1, 1, tzinfo=UTC)
    _advance_clock_fixture(monkeypatch)

    with caplog.at_level("WARNING", logger=_LOGGER):
        out = asyncio.run(scraper._scrape_user(ctx, "alice", since))

    assert out is None
    messages = "\n".join(record.getMessage() for record in caplog.records)
    assert "login gate" in messages.lower()


def test_pw_scrape_user_reloads_on_error_page(
    _patch_pw_scrape_clocks: None,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """In-loop error-page detection: body text containing ``"Something went
    wrong"`` triggers ``page.reload(wait_until="load", timeout=30000)``."""
    page = _FakePage()
    page.evaluate_return_list = ["", "Something went wrong"]
    ctx = _FakeContext(page)
    cfg = TwitterConfig()
    scraper = TwitterPlaywrightScraper(cfg)
    since = datetime(2026, 1, 1, tzinfo=UTC)
    _advance_clock_fixture(monkeypatch)

    out = asyncio.run(scraper._scrape_user(ctx, "alice", since))

    assert out is None
    assert len(page.reload_calls) == 1
    assert page.reload_calls[0]["wait_until"] == "load"
    assert page.reload_calls[0]["timeout"] == 30000


def test_pw_scrape_user_handles_page_goto_timeout_with_retry_loop(
    _patch_pw_scrape_clocks: None,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """``page.goto`` raises a Timeout exception three times; the non-Timeout
    branch is never taken, and the ``if attempt == 2: break`` fires."""
    page = _FakePage()
    page.evaluate_return = ""
    page.goto_exception_message = "Timeout reached after 25s"
    ctx = _FakeContext(page)
    cfg = TwitterConfig()
    scraper = TwitterPlaywrightScraper(cfg)
    since = datetime(2026, 1, 1, tzinfo=UTC)
    _advance_clock_fixture(monkeypatch)

    out = asyncio.run(scraper._scrape_user(ctx, "alice", since))

    assert out is None
    assert page.goto_calls == [
        "https://x.com/alice",
        "https://x.com/alice",
        "https://x.com/alice",
    ]


def test_pw_scrape_user_returns_none_when_page_goto_raises(
    _patch_pw_scrape_clocks: None,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A non-Timeout ``page.goto`` exception on the third attempt re-raises and
    is caught by the outer ``except`` → ``return None`` (``finally`` still runs)."""
    page = _FakePage()
    page.evaluate_return = ""
    page.goto_exception_message = "DNS resolution failed"
    ctx = _FakeContext(page)
    cfg = TwitterConfig()
    scraper = TwitterPlaywrightScraper(cfg)
    since = datetime(2026, 1, 1, tzinfo=UTC)
    _advance_clock_fixture(monkeypatch)

    out = asyncio.run(scraper._scrape_user(ctx, "alice", since))

    assert out is None
    assert page.goto_calls == [
        "https://x.com/alice",
        "https://x.com/alice",
        "https://x.com/alice",
    ]


def test_pw_scrape_user_breaks_polling_loop_when_at_bottom_reached(
    _patch_pw_scrape_clocks: None,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """``at_bottom=True AND (time - start_time) > 20`` breaks the loop early."""
    page = _FakePage()
    page.evaluate_return = ""
    page.scroll_height_break = True
    ctx = _FakeContext(page)
    cfg = TwitterConfig()
    scraper = TwitterPlaywrightScraper(cfg)
    since = datetime(2026, 1, 1, tzinfo=UTC)
    _advance_clock_fixture(monkeypatch)

    out = asyncio.run(scraper._scrape_user(ctx, "alice", since))

    assert out is None


def test_pw_scrape_user_routes_abort_media_and_analytics_but_passes_through(
    _patch_pw_scrape_clocks: None,
) -> None:
    """Production's ``route_handler`` aborts media/image/video and
    analytics/tracking URLs, and passes everything else through."""
    page = _FakePage()
    ctx = _FakeContext(page)
    cfg = TwitterConfig()
    scraper = TwitterPlaywrightScraper(cfg)
    since = datetime(2026, 1, 1, tzinfo=UTC)

    async def _runner() -> list[dict[str, Any]] | None:
        task = asyncio.create_task(scraper._scrape_user(ctx, "alice", since))
        await _yield_n(50)
        await page.dispatch_route("https://pbs.twimg.com/media/aaa.jpg", resource_type="image")
        await page.dispatch_route(
            "https://video.twimg.com/ext_tw_video/123/pu/vid.mp4",
            resource_type="video",
        )
        await page.dispatch_route("https://pbs.twimg.com/media/bbb.mp4", resource_type="media")
        await page.dispatch_route("https://www.google-analytics.com/collect?v=1", resource_type="xhr")
        await page.dispatch_route("https://secure.adnxs.com/doubleclick?id=42", resource_type="xhr")
        await page.dispatch_route("https://scribe.twitter.com/scribe?log=1", resource_type="xhr")
        await page.dispatch_route("https://api.x.com/1.1/users/show.json", resource_type="xhr")
        valid = _make_tweet_payload(
            tweet_id="1001",
            text="hello",
            created_at="Fri Jan 02 12:00:00 +0000 2026",
        )
        await page.dispatch(
            "https://x.com/i/api/graphql/abc/UserTweets?variables=foo",
            _wrap_tweet_envelope(valid),
        )
        return await task

    out = asyncio.run(_runner())

    assert out is not None
    assert len(out) == 1
    assert out[0]["tweet_id"] == "1001"

    aborted_urls = [u for u, _ in page.route_aborted]
    continued_urls = [u for u, _ in page.route_continued]

    assert "https://pbs.twimg.com/media/aaa.jpg" in aborted_urls
    assert "https://video.twimg.com/ext_tw_video/123/pu/vid.mp4" in aborted_urls
    assert "https://pbs.twimg.com/media/bbb.mp4" in aborted_urls
    assert "https://www.google-analytics.com/collect?v=1" in aborted_urls
    assert "https://secure.adnxs.com/doubleclick?id=42" in aborted_urls
    assert "https://scribe.twitter.com/scribe?log=1" in aborted_urls
    assert "https://api.x.com/1.1/users/show.json" in continued_urls
    assert "https://pbs.twimg.com/media/aaa.jpg" not in continued_urls
    assert len(page.route_aborted) == 6
    assert len(page.route_continued) == 1
