"""This file contains the streamlit app for the TSP Dashboard."""

import streamlit as st
from tspdashboard.utilities import generate_instance
import matplotlib.pyplot as plt
import logging


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
        should_instance_be_generated = st.button("Generate Instance")

    if should_instance_be_generated:
        instance = generate_instance(no_cities=int(no_cities))
        st.session_state["instance"] = instance
        logging.debug("Generated instance.")
        logging.debug(instance)

    if st.session_state["instance"] is not None:
        # Make the map column wider than the button column
        col1, col2 = st.columns([3, 1])

        # Plot the instance as coordinates
        fig, ax = plt.subplots()
        ax.plot(
            st.session_state["instance"][:, 0], st.session_state["instance"][:, 1], "o"
        )

        with col1:
            st.pyplot(fig)

        with col2:
            # Add button for optimizing the instance
            should_greedy_optimize = st.button("Greedy solution")

            if should_greedy_optimize:
                st.write("Greedy solution")
                # Optimize the instance using the greedy algorithm
                st.write("Greedy solution")
                st.write("Total distance: 0")


if __name__ == "__main__":
    main()
