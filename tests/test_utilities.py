from tspdashboard.utilities import generate_instance, generate_distance_matrix
import numpy as np
import pytest


def test_generate_instance():
    """Test the generate_instance function which is a bit silly because it is
    basically testing numpy's random.rand function."""
    # Generate an instance
    instance = generate_instance(no_cities=10)

    # Check that the instance is a numpy array
    assert isinstance(instance, np.ndarray)

    # Check that the instance has the correct shape
    assert instance.shape == (10, 2)

    # Check that the values are between 0 and 1
    assert np.all((instance >= 0) & (instance <= 1))


def test_generate_distance_matrix_fails_with_wrong_input():
    """Test the generate_distance_matrix function with wrong input."""
    # Generate a distance matrix with a wrong input
    with pytest.raises(ValueError):
        generate_distance_matrix(cities_coordinates=np.ndarray([1, 2, 3]))


def test_generate_distance_matrix():
    """Test the generate_distance_matrix function."""

    # An easy instance with 3 cities
    instance = np.array([[0, 0], [0.5, 0.5], [1, 1]])

    # Generate a distance matrix
    distance_matrix = generate_distance_matrix(cities_coordinates=instance)

    # Check that the distance matrix is a numpy array
    assert isinstance(distance_matrix, np.ndarray)

    # Check that the distance matrix has the correct shape
    assert distance_matrix.shape == (3, 3)

    # Check that the distance matrix is symmetric
    assert np.all(distance_matrix == distance_matrix.T)

    # Check that the diagonal is zero
    assert np.all(distance_matrix.diagonal() == 0)

    # Check that the values are floats
    assert distance_matrix.dtype == np.float64

    # Check the distance from the first city (0, 0) to (1, 1) which is approx 1.414
    assert 1.41421356 == pytest.approx(distance_matrix[0][2])
