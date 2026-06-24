# tspdashboard

This project is a streamlit app that will allow the user to generate (small) Travelling Salesperson Problems and 
solve them using a variety of algorithms. The app will also display the solution on a map. 

Host on Streamlit https://travellingsalesman.streamlit.app/

## How to run

To run this locally having all the dependencies installed, you can run the following command (using uv):

```uv run streamlit run run_app.py```

Omit the `uv run` if you have the dependencies installed globally or are directly in the virtual environment.


## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. To install the dependencies (including the dev tools), run the following command:

```uv sync```

or use the `requirements.txt` file to install the runtime dependencies using pip:

```pip install -r requirements.txt```

To run formatting, linting and tests use the following command:

```uv run ./run_tests_formatting_and_linting.sh```

The `requirements.txt` file is regenerated from the lockfile by that script via `uv export`. No extra plugins are required.
