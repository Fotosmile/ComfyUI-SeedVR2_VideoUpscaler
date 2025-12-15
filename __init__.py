"""
ComfyUI-SeedVR2_VideoUpscaler
Official SeedVR2 integration for ComfyUI
"""

from .seedvr2_videoupscaler.optimization.compatibility import ensure_triton_compat  # noqa: F401
from .seedvr2_videoupscaler.interfaces import comfy_entrypoint, SeedVR2Extension

__all__ = ["comfy_entrypoint", "SeedVR2Extension"]