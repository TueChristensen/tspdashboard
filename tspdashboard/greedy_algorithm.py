"""A simple greedy algorithm for the TSP problem."""

from typing import Tuple

import numpy as np


def greedy_algorithm(
    distance_matrix: np.ndarray, start_city: int = 0
) -> Tuple[np.ndarray, float]:
    """A simple greedy algorithm for the TSP problem.

    Args:
        distance_matrix (np.ndarray): The distance matrix of the TSP problem.
        start_city (int, optional): The index of the starting city. Defaults to 0.

    Returns:
        Tuple[np.ndarray, float]: A tuple containing the best tour found by the
        greedy algorithm and the total distance of the tour.
    """
    no_cities = distance_matrix.shape[0]
    # Initialize the tour with the first city
    tour = [start_city]
    # Initialize the set of unvisited cities
    unvisited_cities = set(range(no_cities))

    # Remove the starting city
    unvisited_cities.remove(start_city)

    # Initialize the total distance
    total_distance = 0

    # Repeat until all cities have been visited
    while unvisited_cities:
        # Get the last city in the tour
        current_city = tour[-1]
        # Find the nearest unvisited city
        nearest_city = min(
            unvisited_cities, key=lambda city: distance_matrix[current_city, city]
        )
        # Add the nearest city to the tour
        tour.append(nearest_city)
        # Remove the nearest city from the set of unvisited cities
        unvisited_cities.remove(nearest_city)
        # Update the total distance
        total_distance += distance_matrix[current_city, nearest_city]

    # Add the distance back to the starting city
    total_distance += distance_matrix[tour[-1], tour[0]]

    # Add the starting city to the end of the tour
    tour.append(tour[0])

    return np.array(tour), total_distance
