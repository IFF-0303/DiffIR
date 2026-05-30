"""Explicit DiffIR inpainting architecture imports.

Import architectures here in the traditional Python style so callers can use
``import archs`` or ``from archs import DiffIRS1`` without relying on config
strings to discover the available models.
"""

from .S1_arch import DiffIRS1  # noqa: F401
from .S2_arch import DiffIRS2  # noqa: F401

__all__ = ['DiffIRS1', 'DiffIRS2']
