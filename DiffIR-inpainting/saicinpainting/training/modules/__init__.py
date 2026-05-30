import logging

from archs import DiffIRS1, DiffIRS2
from saicinpainting.training.modules.ffc import FFCResNetGenerator
from saicinpainting.training.modules.pix2pixhd import (GlobalGenerator, MultiDilatedGlobalGenerator,
                                                       MultidilatedNLayerDiscriminator, NLayerDiscriminator)

GENERATOR_REGISTRY = {
    'pix2pixhd_multidilated': MultiDilatedGlobalGenerator,
    'pix2pixhd_global': GlobalGenerator,
    'ffc_resnet': FFCResNetGenerator,
    'DiffIRS1': DiffIRS1,
    'DiffIRS2': DiffIRS2,
}

DISCRIMINATOR_REGISTRY = {
    'pix2pixhd_nlayer_multidilated': MultidilatedNLayerDiscriminator,
    'pix2pixhd_nlayer': NLayerDiscriminator,
}


def make_generator(config, kind, **kwargs):
    logging.info(f'Make generator {kind}')

    generator_cls = GENERATOR_REGISTRY.get(kind)
    if generator_cls is None:
        raise ValueError(f'Unknown generator kind {kind}')
    return generator_cls(**kwargs)


def make_discriminator(kind, **kwargs):
    logging.info(f'Make discriminator {kind}')

    discriminator_cls = DISCRIMINATOR_REGISTRY.get(kind)
    if discriminator_cls is None:
        raise ValueError(f'Unknown discriminator kind {kind}')
    return discriminator_cls(**kwargs)


__all__ = ['DISCRIMINATOR_REGISTRY', 'GENERATOR_REGISTRY', 'make_discriminator', 'make_generator']
