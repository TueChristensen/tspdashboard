from tspdashboard.utilities import generate_instance
import numpy as np


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

    # Check that the values are floats
    assert instance.dtype == np.float64
