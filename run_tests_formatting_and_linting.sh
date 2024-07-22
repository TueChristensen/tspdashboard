#!/bin/bash

# You probably need to run this with poetry run bash run_tests_formatting_and_linting.sh

# Run ruff formatting

ruff format .

ruff_exit_code=$?

if [ $ruff_exit_code -ne 0 ]; then

  echo 'Ruff formatting failed, exiting the script'

  exit $ruff_exit_code
fi


# Run the linting

ruff check .

ruff_exit_code=$?

if [ $ruff_exit_code -ne 0 ]; then

  echo 'Ruff linting failed, exiting the script'

  exit $ruff_exit_code
fi

echo ruff successful

# Run the mypy checks

mypy .

mypy_exit_code=$?

if [ $mypy_exit_code -ne 0 ]; then

  echo 'Mypy failed, exiting the script'

  exit $mypy_exit_code
fi

# Run pytest and get the exit code in a param.

pytest .

pytest_exit_code=$?

# The error code 5 is thrown when no tests are found.
if [ $pytest_exit_code -ne 0 ]; then

  echo "Pytest failed, exiting the script with status {$pytest_exit_code}"

  exit $pytest_exit_code
fi

echo Pytest successful

echo Ran all checks successfully, exiting 0
exit 0