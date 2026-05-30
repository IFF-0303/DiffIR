import logging

from saicinpainting.training.visualizers.directory import DirectoryVisualizer
from saicinpainting.training.visualizers.noop import NoopVisualizer

VISUALIZER_REGISTRY = {
    'directory': DirectoryVisualizer,
    'noop': NoopVisualizer,
}


def make_visualizer(kind, **kwargs):
    logging.info(f'Make visualizer {kind}')

    visualizer_cls = VISUALIZER_REGISTRY.get(kind)
    if visualizer_cls is None:
        raise ValueError(f'Unknown visualizer kind {kind}')
    return visualizer_cls(**kwargs)


__all__ = ['VISUALIZER_REGISTRY', 'make_visualizer']
