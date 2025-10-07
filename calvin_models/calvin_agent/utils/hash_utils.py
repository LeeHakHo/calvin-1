"""Lightweight fallback replacement for `pyhash.fnv1_32`.

Provides a callable factory `fnv1_32_hasher()` that matches the
`pyhash.fnv1_32()` behavior used in the codebase: returns a callable
that accepts a string and returns a 32-bit integer hash.

This implementation is pure Python and portable to non-x86 platforms.
"""
from typing import Callable


def fnv1_32(s: str) -> int:
    """Compute FNV-1 32-bit hash for the given string.

    Returns an unsigned 32-bit integer.
    """
    # FNV-1 32-bit parameters
    h = 0x811c9dc5
    fnv_prime = 0x01000193
    data = s.encode("utf-8")
    for b in data:
        h = (h * fnv_prime) & 0xFFFFFFFF
        h ^= b
    return h


def fnv1_32_hasher() -> Callable[[str], int]:
    """Return a callable that computes the fnv1_32 hash for a string.

    Matches the usage pattern `hasher = pyhash.fnv1_32(); hasher(str(idx))`.
    """

    def _hasher(s: str) -> int:
        return fnv1_32(s)

    return _hasher
