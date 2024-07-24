"""Various utility functions for the TSP Dashboard application."""


import numpy as np


def generate_instance(no_cities: int = 10) -> np.ndarray:
    """Generates a new instance of the TSP problem with size of no_cities where all
    cities have locations specified as (x,y) coordinates in the [0.0,1.0) range."""
    gen = np.random.default_rng()
    return gen.random((no_cities, 2))


def generate_distance_matrix(cities_coordinates: np.ndarray) -> np.ndarray:
    """Generates a distance matrix from the coordinates of the cities."""

    # Test that there are cities
    if cities_coordinates.shape[0] <= 1:
        raise ValueError("The cities_coordinates should have at least 2 cities.")

    # Test that the size of the input is correct - it should be an array of
    # shape (no_cities, 2)
    if cities_coordinates.shape[1] != 2:
        raise ValueError("The cities_coordinates should have shape (no_cities, 2).")

    no_cities = cities_coordinates.shape[0]
    distance_matrix = np.zeros((no_cities, no_cities))
    for i in range(no_cities):
        for j in range(no_cities):
            distance_matrix[i, j] = np.linalg.norm(
                cities_coordinates[i] - cities_coordinates[j]
            )

    return distance_matrix
