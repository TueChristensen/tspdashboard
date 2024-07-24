"""This file contains the streamlit app for the TSP Dashboard."""

import streamlit as st

from tspdashboard.exact_mip_agorithm import exact_algorithm
from tspdashboard.utilities import generate_instance, generate_distance_matrix
from tspdashboard.greedy_algorithm import greedy_algorithm
import matplotlib.pyplot as plt
import logging


def clear_session_state() -> None:
    """Clear the session state."""
    st.session_state.clear()
    st.session_state["exact_toggle"] = False
    st.session_state["greedy_toggle"] = False


def greedy_optimize_if_not_in_session_state() -> None:
    """Run the greedy optimization algorithm if the solution is not in the session
    state."""
    if "greedy_solution" not in st.session_state:
        greedy_optimize()


def greedy_optimize() -> None:
    """Run the greedy optimization algorithm."""
    logging.info("Optimizing the instance using the greedy algorithm.")

    # If the distance matrix is not yet calculated, calculate it
    if "instance_distance_matrix" not in st.session_state:
        logging.info("Calculating the distance matrix.")
        distance_matrix = generate_distance_matrix(st.session_state["instance"])
        st.session_state["instance_distance_matrix"] = distance_matrix

    greedy_solution, greedy_objective = greedy_algorithm(
        st.session_state["instance_distance_matrix"], start_city=0
    )

    logging.info("Greedy solution: %s", greedy_solution)
    logging.info("Greedy objective: %s", greedy_objective)

    # Write the info to the session state
    st.session_state["greedy_solution"] = greedy_solution
    st.session_state["greedy_objective"] = greedy_objective


def exact_optimize_if_not_in_session_state() -> None:
    """Run the exact optimization algorithm if the solution is not in the session
    state."""
    if "exact_solution" not in st.session_state:
        exact_optimize()


def exact_optimize() -> None:
    """Run the exact optimization algorithm."""
    logging.info("Optimizing the instance using the exact algorithm.")

    # If the distance matrix is not yet calculated, calculate it
    if "instance_distance_matrix" not in st.session_state:
        logging.info("Calculating the distance matrix.")
        distance_matrix = generate_distance_matrix(st.session_state["instance"])
        st.session_state["instance_distance_matrix"] = distance_matrix

    exact_solution, exact_objective = exact_algorithm(
        st.session_state["instance_distance_matrix"]
    )

    logging.info("Exact solution: %s", exact_solution)
    logging.info("Greedy objective: %s", exact_objective)

    # Write the info to the session state
    st.session_state["exact_solution"] = exact_solution
    st.session_state["exact_objective"] = exact_objective


@st.experimental_fragment
def map_and_solution_plot() -> None:
    """This is inside a fragment to re-draw the plot without re-running the whole
    script.
    """
    instance = st.session_state["instance"]

    # Make the map column wider than the button column
    col1, col2 = st.columns([3, 1])

    # Plot the instance as coordinates
    fig, ax = plt.subplots()
    ax.plot(instance[:, 0], instance[:, 1], "o")

    # If there is a greedy solution, plot it in red
    if (
        "greedy_solution" in st.session_state
        and st.session_state["greedy_solution"] is not None
    ) and st.session_state["greedy_toggle"]:
        ax.plot(
            instance[st.session_state["greedy_solution"], 0],
            instance[st.session_state["greedy_solution"], 1],
            "r-",
        )

    # If there is an exact solution, plot it in green
    if (
        "exact_solution" in st.session_state
        and st.session_state["exact_solution"] is not None
        and st.session_state["exact_toggle"]
    ):
        ax.plot(
            instance[st.session_state["exact_solution"], 0],
            instance[st.session_state["exact_solution"], 1],
            "g-",
        )

    with col1:
        st.pyplot(fig)

    with col2:
        # Add a button for optimizing the instance using the greedy algorithm
        st.toggle(
            "Greedy solution",
            on_change=greedy_optimize_if_not_in_session_state,
            key="greedy_toggle",
        )

        # Add a button for optimizing the instance using the exact algorithm
        st.toggle(
            "Exact solution",
            on_change=exact_optimize_if_not_in_session_state,
            key="exact_toggle",
        )


def main() -> None:
    """Main function for the streamlit app."""
    st.write("# TSP Dashboard")
    st.write(
        "Welcome to the TSP Dashboard! This dashboard is designed to help you "
        "visualize the performance of different algorithms on the "
        "travelling salesperson "
        "problem. To get started, "
        "please generate and optimize an instance using the buttons below."
    )

    if "instance" not in st.session_state:
        # Initialize the session state
        st.session_state["instance"] = None

    # Add buttons to generate an instance

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("Number of cities:")
    with col2:
        # Get the input from the user for the number of cities
        no_cities = st.number_input(
            "Number of cities",
            placeholder="Number of cities",
            min_value=2,
            value=10,
            max_value=50,
            label_visibility="collapsed",
        )
    with col3:
        should_instance_be_generated = st.button("Generate Instance", key="generate")

    if should_instance_be_generated:
        # Clear the session state to remove old data
        clear_session_state()

        instance = generate_instance(no_cities=int(no_cities))
        st.session_state["instance"] = instance
        logging.debug("Generated instance.")
        logging.debug(instance)

    if st.session_state["instance"] is not None:
        st.session_state["toggle_greedy"] = False
        st.session_state["toggle_exact"] = False

        map_and_solution_plot()


if __name__ == "__main__":
    main()
