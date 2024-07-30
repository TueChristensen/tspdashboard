# tspdashboard

This project is a streamlit app that will allow the user to generate (small) Travelling Salesperson Problems and 
solve them using a variety of algorithms. The app will also display the solution on a map. 


## How to run

To run this locally having all the dependencies installed, you can run the following command (using poetry):

```poetry run streamlit run tspdashboard/main.py```

Omit the `poetry run` if you have the dependencies installed globally or are directly in the virtual environment.


## Development

This project uses poetry for dependency management. To install the dependencies, run the following command:

```poetry install```

or use the `requirements.txt` file to install the dependencies using pip:

```pip install -r requirements.txt```

To run formatting, linting and tests use the following command:

``` poetry run ./run_tests_formatting_and_linting.sh```

You NEED the plugin for freezing dependencies to work. To install it, run the following command:

```poetry self add poetry-plugin-export``` 
