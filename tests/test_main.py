"""Phase 4 unit tests for ``src.main`` CLI entrypoint.

Covers the happy path (``main`` calls ``orchestrator.run``), and the various
``sys.exit(N)`` branches: missing ``config.json`` (with/without
``config.example.json`` template), ``ConfigError``, generic exceptions, and
``KeyboardInterrupt``. ``print_config_template`` is exercised as a sanity
check that it does not crash.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.main import _parse_args, main, print_config_template
from src.storage.manager import ConfigError

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _minimal_config_bytes() -> bytes:
    payload: dict[str, Any] = {
        "ai": {
            "provider": "openai",
            "model": "deepseek-chat",
            "api_key_env": "OPENAI_API_KEY",
            "temperature": 0.3,
            "max_tokens": 4096,
        },
        "sources": {
            "hackernews": {"enabled": True},
            "reddit": {"enabled": False, "subreddits": [], "users": []},
            "telegram": {"enabled": False, "channels": []},
            "ossinsight": {"enabled": False},
        },
    }
    return json.dumps(payload).encode("utf-8")


@pytest.fixture
def minimal_config(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Change CWD to a tmp dir with a valid ``data/config.json``."""

    monkeypatch.chdir(tmp_path)
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "config.json").write_bytes(_minimal_config_bytes())
    return tmp_path


def _patch_main(monkeypatch: pytest.MonkeyPatch, fake_orchestrator: MagicMock) -> None:
    """Wire up the fake orchestrator + storage so ``main()`` can run."""

    monkeypatch.setattr("src.main.HorizonOrchestrator", lambda *_a, **_kw: fake_orchestrator)


def _async_run_sync(coro_unused: Any) -> Any:
    """Replace ``asyncio.run`` so it pops the coroutine's await immediately.

    Tests pass ``fake_run = AsyncMock(return_value=None)`` so calling
    ``fake_run()`` returns a coroutine that immediately resolves to None.
    """
    return None


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------


def test_main_runs_orchestrator_with_no_args(minimal_config: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fake_run = AsyncMock(return_value=None)
    fake_orchestrator = MagicMock()
    fake_orchestrator.run = fake_run

    _patch_main(monkeypatch, fake_orchestrator)
    monkeypatch.setattr("src.main.asyncio.run", _async_run_sync)
    monkeypatch.setattr(
        "src.main._parse_args",
        lambda argv=None: argparse.Namespace(hours=None, data_dir='data', config=None, log_level='WARNING'),
    )

    main()
    fake_run.assert_called_once_with(force_hours=None)


def test_main_passes_force_hours_to_orchestrator(minimal_config: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fake_run = AsyncMock(return_value=None)
    fake_orchestrator = MagicMock()
    fake_orchestrator.run = fake_run

    _patch_main(monkeypatch, fake_orchestrator)
    monkeypatch.setattr("src.main.asyncio.run", _async_run_sync)
    monkeypatch.setattr(
        "src.main._parse_args",
        lambda argv=None: argparse.Namespace(hours=12, data_dir='data', config=None, log_level='WARNING'),
    )

    main()
    fake_run.assert_called_once_with(force_hours=12)


# ---------------------------------------------------------------------------
# sys.exit branches
# ---------------------------------------------------------------------------


def test_main_exits_when_config_missing_without_template(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    (tmp_path / "data").mkdir()
    monkeypatch.setattr(
        "src.main._parse_args",
        lambda argv=None: argparse.Namespace(hours=None, data_dir='data', config=None, log_level='WARNING'),
    )

    with patch("sys.exit", side_effect=SystemExit(1)) as exit_mock, pytest.raises(SystemExit):
        main()
    exit_mock.assert_called_with(1)


def test_main_exits_when_config_missing_with_template(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """``config.example.json`` exists → main() prints hint + exits."""

    monkeypatch.chdir(tmp_path)
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "config.example.json").write_text("{}", encoding="utf-8")
    monkeypatch.setattr(
        "src.main._parse_args",
        lambda argv=None: argparse.Namespace(hours=None, data_dir='data', config=None, log_level='WARNING'),
    )

    with patch("sys.exit", side_effect=SystemExit(1)) as exit_mock, pytest.raises(SystemExit):
        main()
    exit_mock.assert_called_with(1)


def test_main_exits_when_storage_load_config_raises_config_error(
    minimal_config: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fake_storage = MagicMock()
    fake_storage.load_config.side_effect = ConfigError("bad")
    monkeypatch.setattr("src.main.StorageManager", lambda data_dir: fake_storage)
    monkeypatch.setattr(
        "src.main._parse_args",
        lambda argv=None: argparse.Namespace(hours=None, data_dir='data', config=None, log_level='WARNING'),
    )

    with patch("sys.exit", side_effect=SystemExit(1)) as exit_mock, pytest.raises(SystemExit):
        main()
    exit_mock.assert_called_with(1)


def test_main_exits_when_storage_load_config_raises_generic_exception(
    minimal_config: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fake_storage = MagicMock()
    fake_storage.load_config.side_effect = RuntimeError("boom")
    monkeypatch.setattr("src.main.StorageManager", lambda data_dir: fake_storage)
    monkeypatch.setattr(
        "src.main._parse_args",
        lambda argv=None: argparse.Namespace(hours=None, data_dir='data', config=None, log_level='WARNING'),
    )

    with patch("sys.exit", side_effect=SystemExit(1)) as exit_mock, pytest.raises(SystemExit):
        main()
    exit_mock.assert_called_with(1)


def test_main_keyboard_interrupt_exits_zero(minimal_config: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fake_orchestrator = MagicMock()
    fake_orchestrator.run = AsyncMock(side_effect=KeyboardInterrupt)
    _patch_main(monkeypatch, fake_orchestrator)
    monkeypatch.setattr(
        "src.main._parse_args",
        lambda argv=None: argparse.Namespace(hours=None, data_dir='data', config=None, log_level='WARNING'),
    )

    with patch("sys.exit", side_effect=SystemExit(0)) as exit_mock, pytest.raises(SystemExit):
        main()
    exit_mock.assert_called_with(0)


def test_main_generic_orchestrator_exception_exits_one(minimal_config: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fake_orchestrator = MagicMock()
    fake_orchestrator.run = AsyncMock(side_effect=RuntimeError("crashed"))
    _patch_main(monkeypatch, fake_orchestrator)
    monkeypatch.setattr(
        "src.main._parse_args",
        lambda argv=None: argparse.Namespace(hours=None, data_dir='data', config=None, log_level='WARNING'),
    )

    with patch("sys.exit", side_effect=SystemExit(1)) as exit_mock, pytest.raises(SystemExit):
        main()
    exit_mock.assert_called_with(1)


# ---------------------------------------------------------------------------
# print_config_template smoke
# ---------------------------------------------------------------------------


def test_print_config_template_does_not_raise() -> None:
    print_config_template()


# ---------------------------------------------------------------------------
# ``_parse_args`` seam (PR >=5 main-001)
#
# Direct--seam tests that bypass ``main()`` and exercise the free function
# in isolation. They monkeypatch ``sys.argv`` so argparse's default-argv
# path does not collide with pytest's own CLI.
# ---------------------------------------------------------------------------


def test_parse_args_with_hours_returns_namespace(monkeypatch: pytest.MonkeyPatch) -> None:
    """``_parse_args(['--hours', '12'])`` returns ``Namespace(hours=12)``."""

    monkeypatch.setattr("sys.argv", ["src.main"])
    assert _parse_args(["--hours", "12"]) == argparse.Namespace(
        hours=12, data_dir="data", config=None, log_level="WARNING"
    )


def test_parse_args_no_args_returns_default_none(monkeypatch: pytest.MonkeyPatch) -> None:
    """``_parse_args([])`` returns ``Namespace(hours=None)`` (no flag given)."""

    monkeypatch.setattr("sys.argv", ["src.main"])
    assert _parse_args([]) == argparse.Namespace(
        hours=None, data_dir="data", config=None, log_level="WARNING"
    )


def test_parse_args_default_argv_uses_sys_argv(monkeypatch: pytest.MonkeyPatch) -> None:
    """``_parse_args()`` with no argv falls through to ``sys.argv[1:]``."""

    monkeypatch.setattr("sys.argv", ["src.main"])
    assert _parse_args() == argparse.Namespace(
        hours=None, data_dir="data", config=None, log_level="WARNING"
    )


def test_parse_args_negative_hours_is_valid(monkeypatch: pytest.MonkeyPatch) -> None:
    """``--hours -1`` is accepted (``type=int`` does not clamp sign)."""

    monkeypatch.setattr("sys.argv", ["src.main"])
    assert _parse_args(["--hours", "-1"]) == argparse.Namespace(
        hours=-1, data_dir="data", config=None, log_level="WARNING"
    )


def test_parse_args_invalid_hours_string_exits_two(monkeypatch: pytest.MonkeyPatch) -> None:
    """``--hours abc`` triggers argparse's standard exit code 2."""

    monkeypatch.setattr("sys.argv", ["src.main"])
    with pytest.raises(SystemExit) as exc_info:
        _parse_args(["--hours", "abc"])
    assert exc_info.value.code == 2


def test_parse_args_help_flag_exits_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    """``--help`` triggers argparse's standard exit code 0 after printing help."""

    monkeypatch.setattr("sys.argv", ["src.main"])
    with pytest.raises(SystemExit) as exc_info:
        _parse_args(["--help"])
    assert exc_info.value.code == 0


def test_parse_args_unknown_flag_exits_two(monkeypatch: pytest.MonkeyPatch) -> None:
    """An unknown flag triggers argparse's standard exit code 2."""

    monkeypatch.setattr("sys.argv", ["src.main"])
    with pytest.raises(SystemExit) as exc_info:
        _parse_args(["--bogus"])
    assert exc_info.value.code == 2


# ---------------------------------------------------------------------------
# Upstream CLI flag forwarding tests (merged from upstream/main)
# ---------------------------------------------------------------------------

from types import SimpleNamespace  # noqa: E402

from src import main as main_module  # noqa: E402


def test_missing_custom_config_reports_requested_path(monkeypatch, tmp_path):
    config_path = tmp_path / "custom" / "horizon.json"

    class MissingConfigStorage:
        def __init__(self, data_dir, config_path):
            self.config_path = Path(config_path)

        def load_config(self):
            raise FileNotFoundError

    output = []
    monkeypatch.setattr(main_module, "StorageManager", MissingConfigStorage)
    monkeypatch.setattr(main_module, "configure_logging", lambda console, level=None: None)
    monkeypatch.setattr(
        main_module,
        "console",
        SimpleNamespace(
            print=lambda *args, **kwargs: output.append(" ".join(map(str, args)))
        ),
    )
    monkeypatch.setattr("sys.argv", ["horizon", "--config", str(config_path)])

    with pytest.raises(SystemExit) as exc_info:
        main_module.main()

    rendered = "\n".join(output)
    assert exc_info.value.code == 1
    assert str(config_path) in rendered
    assert "horizon-wizard" not in rendered


def test_data_dir_and_config_flags_are_forwarded_to_storage_manager(monkeypatch, tmp_path):
    data_dir = tmp_path / "state"
    config_path = tmp_path / "custom" / "horizon.json"
    storage_calls = []

    class RecordingStorage:
        def __init__(self, data_dir, config_path):
            storage_calls.append({"data_dir": data_dir, "config_path": config_path})

        def load_config(self):
            raise FileNotFoundError

    monkeypatch.setattr(main_module, "StorageManager", RecordingStorage)
    monkeypatch.setattr(main_module, "configure_logging", lambda console, level=None: None)
    monkeypatch.setattr(main_module.console, "print", lambda *args, **kwargs: None)
    monkeypatch.setattr(
        "sys.argv",
        ["horizon", "--data-dir", str(data_dir), "--config", str(config_path)],
    )

    with pytest.raises(SystemExit):
        main_module.main()

    assert storage_calls == [{"data_dir": str(data_dir), "config_path": str(config_path)}]


def test_data_dir_and_config_default_to_data_directory(monkeypatch):
    storage_calls = []

    class RecordingStorage:
        def __init__(self, data_dir, config_path):
            storage_calls.append({"data_dir": data_dir, "config_path": config_path})

        def load_config(self):
            raise FileNotFoundError

    monkeypatch.setattr(main_module, "StorageManager", RecordingStorage)
    monkeypatch.setattr(main_module, "configure_logging", lambda console, level=None: None)
    monkeypatch.setattr(main_module.console, "print", lambda *args, **kwargs: None)
    monkeypatch.setattr("sys.argv", ["horizon"])

    with pytest.raises(SystemExit):
        main_module.main()

    assert storage_calls == [{"data_dir": "data", "config_path": None}]


def test_log_level_flag_is_forwarded_to_configure_logging(monkeypatch, tmp_path):
    logging_calls = []

    class RecordingStorage:
        def __init__(self, data_dir, config_path):
            pass

        def load_config(self):
            raise FileNotFoundError

    monkeypatch.setattr(main_module, "StorageManager", RecordingStorage)
    monkeypatch.setattr(
        main_module,
        "configure_logging",
        lambda console, level=None: logging_calls.append(level),
    )
    monkeypatch.setattr(main_module.console, "print", lambda *args, **kwargs: None)
    monkeypatch.setattr("sys.argv", ["horizon", "--log-level", "debug"])

    with pytest.raises(SystemExit):
        main_module.main()

    # The first call is the pre-argparse default; the second reflects the CLI flag.
    assert logging_calls[-1] == "DEBUG"
