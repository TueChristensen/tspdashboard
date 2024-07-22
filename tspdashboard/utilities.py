"""Various utility functions for the TSP Dashboard application."""

from typing import Any

import numpy as np


def generate_instance(no_cities: int = 10) -> Any:
    """Generates a new instance of the TSP problem with size."""
    gen = np.random.default_rng()
    return gen.random((no_cities, 2))
