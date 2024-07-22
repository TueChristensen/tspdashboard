"""This file contains the streamlit app for the TSP Dashboard."""

import streamlit as st
from tspdashboard.utilities import generate_instance
import matplotlib.pyplot as plt
import logging


def main() -> None:
    """Main function for the streamlit app."""
    st.title("# TSP Dashboard")
    st.write(
        "Welcome to the TSP Dashboard! This dashboard is designed to help you "
        "visualize the performance of different algorithms on the "
        "travelling salesperson "
        "problem. To get started, "
        "please generate and optimize an instance using the buttons below."
    )

    # Button for resetting the instance generated/optimized
    should_reset = st.button("Reset", type="primary")

    if should_reset:
        st.session_state["instance"] = None

    # Add buttons to generate an instance
    should_instance_be_generated = st.button("Generate Instance")

    if should_instance_be_generated and st.session_state["instance"] is None:
        instance = generate_instance(no_cities=10)
        st.session_state["instance"] = instance
        logging.debug("Generated instance.")
        logging.debug(instance)

    if st.session_state["instance"] is not None:

        col1, col2 = st.columns(2)

        # Plot the instance as coordinates
        fig, ax = plt.subplots()
        ax.plot(
            st.session_state["instance"][:, 0], st.session_state["instance"][:, 1], "o"
        )

        with col1:
            st.pyplot(fig)

        with col2:
            # Add button for optimizing the instance
            should_optimize = st.button("Greedy solution")

if __name__ == "__main__":
    main()
