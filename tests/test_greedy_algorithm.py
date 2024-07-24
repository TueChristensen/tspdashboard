"""Test the greedy algorithm for the TSP problem."""

import numpy as np

from tspdashboard.greedy_algorithm import greedy_algorithm


def test_greedy_algorithm():
    """Test the greedy_algorithm function."""
    # A simple distance matrix which should yield 0 -> 1 -> 2 -> 0 with a total distance
    # of 6
    distance_matrix = np.array([[0, 1, 2], [1, 0, 3], [2, 3, 0]])

    # Run the greedy algorithm
    tour, total_distance = greedy_algorithm(distance_matrix=distance_matrix)

    # Check that the tour is a numpy array
    assert isinstance(tour, np.ndarray)

    # Check that the tour has the correct shape
    assert tour.shape == (4,)

    # Check that the tour is [0, 1, 2, 0]
    assert np.array_equal(tour, np.array([0, 1, 2, 0]))

    # Check that the total distance is correct
    assert total_distance == 6


def test_greedy_starting_city():
    """Test that setting the starting city yields the correct tour."""
    # A simple distance matrix which should yield 1 -> 0 -> 2 -> 1 with a total distance
    # of 6
    distance_matrix = np.array([[0, 1, 2], [1, 0, 3], [2, 3, 0]])

    # Run the greedy algorithm with the starting city 1
    tour, total_distance = greedy_algorithm(
        distance_matrix=distance_matrix, start_city=1
    )

    # Check that the tour is a numpy array
    assert isinstance(tour, np.ndarray)

    # Check that the tour has the correct shape
    assert tour.shape == (4,)

    # Check that the tour is [1, 0, 2, 1]
    assert np.array_equal(tour, np.array([1, 0, 2, 1]))

    # Check that the total distance is correct
    assert total_distance == 6
