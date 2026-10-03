"""Base extractor interface."""

from abc import ABC, abstractmethod

import httpx


class BaseExtractor(ABC):
    @abstractmethod
    async def extract(self, url: str, client: httpx.AsyncClient) -> str | None:
        """Fetch and extract article text from url. Returns None on failure."""
