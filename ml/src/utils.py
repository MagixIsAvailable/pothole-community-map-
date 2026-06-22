"""General utilities: seed, device detection, timer."""

import random
import time
from contextlib import contextmanager
from typing import Generator

import numpy as np
import torch


def set_seed(seed: int = 42) -> None:
    """Set random seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def get_device() -> str:
    """Return the best available torch device."""
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


@contextmanager
def timer(name: str = "block") -> Generator[None, None, None]:
    """Context manager to time a code block."""
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"[TIMER] {name}: {elapsed:.2f}s")
