"""
SeedVR2 VideoUpscaler
Official SeedVR2 integration for ComfyUI
"""

__version__ = "2.5.20"
__all__ = []

try:
    from .optimization.compatibility import ensure_triton_compat  # noqa: F401
except ImportError:
    pass  # Optional dependency
