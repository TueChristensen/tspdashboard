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

To run formatting, linting and tests use the following command:

``` poetry run ./run_tests_formatting_and_linting.sh```

## Todo

1. Add metrics for the greedy and optimal
1. Add test for the main app
1. Dockerize the app with buildx for multi-arch support
1. Update readme with 
   1. How to run the app
   2. Formatting and linting
   
