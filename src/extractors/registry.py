"""Extractor registry."""


from ..models import ExtractorConfig, ExtractorType, TrafilaturaExtractorConfig
from .base import BaseExtractor
from .trafilatura import TrafilaturaExtractor

_DEFAULTS: dict[str, ExtractorConfig] = {
    ExtractorType.TRAFILATURA: TrafilaturaExtractorConfig(),
}


def _build(cfg: ExtractorConfig) -> BaseExtractor:
    match cfg:
        case TrafilaturaExtractorConfig():
            return TrafilaturaExtractor(cfg)
        case _:
            raise NotImplementedError(f"Extractor type '{cfg.type}' is not yet implemented")


class ExtractorRegistry:
    def __init__(self, config: dict[str, ExtractorConfig]):
        self._extractors: dict[str, BaseExtractor] = {
            name: _build(cfg) for name, cfg in _DEFAULTS.items()
        }
        self._extractors.update({
            name: _build(cfg) for name, cfg in config.items()
        })

    def get(self, name: str) -> BaseExtractor | None:
        return self._extractors.get(name)
