import logging

import torch

from saicinpainting.evaluation.evaluator import InpaintingEvaluatorOnline, lpips_fid100_f1, ssim_fid100_f1
from saicinpainting.evaluation.losses.base_loss import FIDScore, LPIPSScore, SSIMScore

EVALUATOR_REGISTRY = {
    'default': InpaintingEvaluatorOnline,
}

INTEGRAL_FUNC_REGISTRY = {
    'ssim_fid100_f1': ssim_fid100_f1,
    'lpips_fid100_f1': lpips_fid100_f1,
}


def make_evaluator(kind='default', ssim=True, lpips=True, fid=True, integral_kind=None, **kwargs):
    logging.info(f'Make evaluator {kind}')
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    metrics = {}
    if ssim:
        metrics['ssim'] = SSIMScore()
    if lpips:
        metrics['lpips'] = LPIPSScore()
    if fid:
        metrics['fid'] = FIDScore().to(device)

    if integral_kind is None:
        integral_func = None
    else:
        integral_func = INTEGRAL_FUNC_REGISTRY.get(integral_kind)
        if integral_func is None:
            raise ValueError(f'Unexpected integral_kind={integral_kind}')

    evaluator_cls = EVALUATOR_REGISTRY.get(kind)
    if evaluator_cls is None:
        raise ValueError(f'Unexpected evaluator kind={kind}')
    return evaluator_cls(scores=metrics, integral_func=integral_func, integral_title=integral_kind, **kwargs)


__all__ = ['EVALUATOR_REGISTRY', 'INTEGRAL_FUNC_REGISTRY', 'make_evaluator']
