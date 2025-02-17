# src/test/test_assignment_2.py

import pytest
from src.main.assignment_2 import neville, newton_forward_diff_table, newton_interpolation, hermite_interpolation, cubic_spline_matrix

def test_neville():
    x_vals = [3.6, 3.8, 3.9]
    y_vals = [1.675, 1.436, 1.318]
    x = 3.7
    # Call function
    neville(x_vals, y_vals, x)

def test_newton_interpolation():
    x_vals = [7.2, 7.4, 7.5, 7.6]
    y_vals = [23.5492, 25.3913, 26.8224, 27.4589]
    x = 7.3
    # Call function
    newton_interpolation(x_vals, y_vals, x)

def test_hermite_interpolation():
    x_vals = [3.6, 3.8, 3.9]
    y_vals = [1.675, 1.436, 1.318]
    dy_vals = [-1.195, -1.188, -1.182]
    # Call function
    hermite_interpolation(x_vals, y_vals, dy_vals)

def test_cubic_spline_matrix():
    x_vals = [2, 5, 8, 10]
    y_vals = [3, 5, 7, 9]
    # Call function
    cubic_spline_matrix(x_vals, y_vals)
