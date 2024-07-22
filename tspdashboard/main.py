"""This file contains the streamlit app for the TSP Dashboard."""

import streamlit as st


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


if __name__ == "__main__":
    main()
