"""TSNE importer that prefers MulticoreTSNE when present, otherwise falls
back to sklearn.manifold.TSNE. This avoids hard dependency on MulticoreTSNE
which requires native build tools and CMake.
"""
from typing import Any

try:
    from MulticoreTSNE import MulticoreTSNE as _MTSNE  # type: ignore

    class TSNE(_MTSNE):
        pass

except Exception:
    # Fallback to sklearn implementation
    try:
        from sklearn.manifold import TSNE as _SKTSNE

        class TSNE(_SKTSNE):
            def __init__(self, n_jobs: int = 1, *args: Any, **kwargs: Any):
                # sklearn TSNE doesn't accept n_jobs; accept it for compatibility
                if "n_jobs" in kwargs:
                    kwargs.pop("n_jobs")
                super().__init__(*args, **kwargs)

    except Exception:
        raise ImportError("No TSNE implementation available. Install MulticoreTSNE or scikit-learn.")

__all__ = ["TSNE"]
