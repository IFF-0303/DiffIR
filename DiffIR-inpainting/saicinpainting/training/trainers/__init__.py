import logging

import torch

from saicinpainting.training.trainers.defaultS1 import DefaultInpaintingTrainingModule
from saicinpainting.training.trainers.defaultS2 import SDefaultInpaintingTrainingModule

TRAINING_MODEL_REGISTRY = {
    'defaultS1': DefaultInpaintingTrainingModule,
    'defaultS2': SDefaultInpaintingTrainingModule,
}


def get_training_model_class(kind):
    model_cls = TRAINING_MODEL_REGISTRY.get(kind)
    if model_cls is None:
        raise ValueError(f'Unknown trainer module {kind}')
    return model_cls


def make_training_model(config):
    kind = config.training_model.kind

    kwargs = dict(config.training_model)
    kwargs.pop('kind')
    kwargs['use_ddp'] = config.trainer.kwargs.get('accelerator', None) == 'ddp'

    logging.info(f'Make training model {kind}')

    cls = get_training_model_class(kind)
    return cls(config, **kwargs)


def load_checkpoint(train_config, path, map_location='cuda', strict=True):
    model: torch.nn.Module = make_training_model(train_config)
    state = torch.load(path, map_location=map_location)
    model.load_state_dict(state['state_dict'], strict=strict)
    model.on_load_checkpoint(state)
    return model


__all__ = ['TRAINING_MODEL_REGISTRY', 'get_training_model_class', 'load_checkpoint', 'make_training_model']
