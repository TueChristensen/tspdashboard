"""This tests that the main app runs and can generate instances and solve them."""

from streamlit.testing.v1 import AppTest


def test_app_workflow() -> None:
    """Main test that the app can run and 'correct' usage works."""

    # Load the app from the main module
    at = AppTest.from_file("../tspdashboard/app.py")

    # Run the app and assert that it runs without errors
    at.run()
    assert not at.exception

    # Assert that there is no instance in the session state
    assert at.session_state["instance"] is None

    # Click the generate instance button (with default parameters) and assert that the
    # instance is generated
    at.button(key="generate").click().run()

    assert at.session_state["instance"] is not None

    # Now we are ready to run the algorithms. First lets check that there is now
    # metrics in the session state
    assert len(at.metric) == 0

    # Now toggle the greedy algorithm and assert that the greedy solution is generated

    assert at.session_state["greedy_toggle"] is False
    assert "greedy_solution" not in at.session_state

    at.toggle(key="greedy_toggle").set_value(True).run()

    assert at.session_state["greedy_toggle"] is True
    assert at.session_state["greedy_solution"] is not None

    # Now toggle the exact algorithm and assert that the exact solution is generated

    assert at.session_state["exact_toggle"] is False
    assert "exact_solution" not in at.session_state

    at.toggle(key="exact_toggle").set_value(True).run()

    assert at.session_state["exact_toggle"] is True
    assert at.session_state["exact_solution"] is not None

    # Now we should have metrics in the session state
    assert len(at.metric) > 0
