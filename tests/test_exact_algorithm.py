"""Test the exact algorithm for the TSP problem."""

import numpy as np

from tspdashboard.exact_mip_agorithm import exact_algorithm


def test_exact_algorithm():
    """Test the exact_algorithm function."""
    # A simple distance matrix which should yield 0 -> 1 -> 2 -> 0 with a total distance
    # of 6
    distance_matrix = np.array([[0, 1, 2], [1, 0, 3], [2, 3, 0]])

    # Run the exact algorithm
    tour, total_distance = exact_algorithm(distance_matrix=distance_matrix)

    # Check that the tour is a numpy array
    assert isinstance(tour, list)

    # Check that the tour has the correct shape
    assert len(tour) == 4

    # Check that the tour is [0, 1, 2, 0]
    assert np.array_equal(tour, np.array([0, 1, 2, 0]))

    # Check that the total distance is correct
    assert int(total_distance) == 6
