from typing import Tuple, List

import numpy as np
from ortools.math_opt.python import mathopt
import time
from datetime import timedelta
import logging

log = logging.getLogger(__name__)


def build_model(distance_matrix: np.ndarray) -> Tuple[mathopt.Model, dict]:
    # Build the model.
    model = mathopt.Model(name="TSP")

    # Add variables
    x = {}
    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix[i])):
            if i != j:
                x[i, j] = model.add_binary_variable(name=f"x[{i},{j}]")
            else:
                x[i, j] = model.add_variable(name=f"x[{i},{j}]", lb=0, ub=0)

    # Add constraints (in-degree 1 and out-degree 1)
    for i in range(len(distance_matrix)):
        model.add_linear_constraint(
            mathopt.fast_sum(x[i, j] for j in range(len(distance_matrix))) == 1
        )

    for j in range(len(distance_matrix)):
        model.add_linear_constraint(
            mathopt.fast_sum(x[i, j] for i in range(len(distance_matrix))) == 1
        )

    # Add subtour elimination constraints of by Gavish and Graves (1978)
    f = {}
    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix[i])):
            f[i, j] = model.add_variable(
                name=f"f[{i},{j}]", lb=0, ub=len(distance_matrix)
            )

    # Add constraints for the "one commodity flow" formulation
    for i in range(1, len(distance_matrix)):
        model.add_linear_constraint(
            mathopt.fast_sum(f[i, j] - f[j, i] for j in range(len(distance_matrix)))
            == 1
        )

    # Add constraints for the "one commodity flow" formulation
    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix)):
            model.add_linear_constraint(f[i, j] <= (len(distance_matrix) - 1) * x[i, j])

    # Add objective
    model.minimize_linear_objective(
        mathopt.LinearSum(
            distance_matrix[i][j] * x[i, j]
            for i in range(len(distance_matrix))
            for j in range(len(distance_matrix[i]))
        )
    )

    return model, x


def exact_algorithm(
    distance_matrix: np.ndarray,
    solver_type: mathopt.SolverType = mathopt.SolverType.GSCIP,
    solve_time_limit: timedelta = timedelta(seconds=30),
) -> Tuple[List[int], float]:
    """Build a TSP model and solve it using the given solver type."""

    # Build a model
    model, x = build_model(distance_matrix)

    # Set parameters, e.g. turn on logging.
    params = mathopt.SolveParameters(enable_output=False, time_limit=solve_time_limit)

    # Time the model solving
    start = time.time()

    # Solve the model
    result = mathopt.solve(model, solver_type, params=params)

    if result.termination.reason not in (
        mathopt.TerminationReason.OPTIMAL,
        mathopt.TerminationReason.FEASIBLE,
    ):
        raise RuntimeError(f"model failed to solve: {result.termination}")

    solution_time = time.time() - start

    log.info("Time: %s seconds", solution_time)

    # Extract the solution
    extracted_sol = []
    next_city = 0

    extracted_sol.append(next_city)

    while len(extracted_sol) < len(distance_matrix):
        for j in range(len(distance_matrix)):
            if result.variable_values()[x[next_city, j]] > 0.5:
                next_city = j
                extracted_sol.append(next_city)
                break

    # Add the starting city to the end of the tour
    extracted_sol.append(extracted_sol[0])

    log.info("Extracted solution: %s", extracted_sol)

    # Return the solution and the objective value
    return extracted_sol, result.best_objective_bound()
