"""Specify the simulation design in one place."""

import numpy as np

def _make_id(*things):
    return "_".join(things.values())

def make_scenarios():
    """Return {scenario_id: settings} for experiments A and B.

    IDs are unique, stable, filename-safe strings. Each settings dictionary
    has exactly experiment ('A'/'B'), n (int), p (int), rho (float), and
    error_distribution ('normal'/'laplace'). Assume 0 < p < n, 0 <= rho < 1.
    The study supplies all generation, fitting, evaluation, and replication.

    Keep n=200. For A, use rho=0 and both error laws over the SAME chosen
    p/n values. For B, use normal errors and p=100 and choose rho values.
    Choose the values yourselves; the handout grid is only an example.
    """

    N = 200

    scenarios = {}

    # Question A
    for p in (1, 10, 50, 100, 200):
        for error_dist in ('normal'/'laplace'):
            scenario_without_id = {
                "experiment": "A",
                "n": N,
                "p" : p,
                "rho" : 0,
                "error_distribution" : error_dist,
            }
            scenarios.add({_make_id(scenario_without_id)} + scenario_without_id)

    # Question B
    for rho in np.linspace(0,1,20):
        scenario_without_id = {
            "experiment": "B",
            "n": N,
            "p" : 100,
            "rho" : rho,
            "error_distribution" : "normal",
        }
        scenarios.add({_make_id(scenario_without_id)} + scenario_without_id)

    return scenarios