# src/test/test_assignment_2.py
import sys
import os
import unittest

# Added the root directory to system path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.main.assignment_2 import neville, newton_forward_diff_table, newton_interpolation, hermite_interpolation, cubic_spline_matrix

class TestAssignment2(unittest.TestCase):
    def test_neville(self):
        # Example test case for neville function
        x_vals = [1, 2, 3]
        y_vals = [1, 4, 9]
        x = 2.5
        result = neville(x_vals, y_vals, x)
        print(f"Test Neville: {result}")  # Print the result
        

    def test_newton_interpolation(self):
        # Example test case for newton_interpolation function
        x_vals = [1, 2, 3]
        y_vals = [1, 4, 9]
        x = 2.5
        result = newton_interpolation(x_vals, y_vals, x)
        print(f"Test Newton Interpolation: {result}")  # Print the result
        

    def test_hermite_interpolation(self):
        # Example test case for hermite_interpolation function
        x_vals = [1, 2, 3]
        y_vals = [1, 4, 9]
        dy_vals = [1, 2, 3]
        result = hermite_interpolation(x_vals, y_vals, dy_vals)
        print(f"Test Hermite Interpolation: {result}")  # Print the result
        

    def test_cubic_spline_matrix(self):
        # Example test case for cubic_spline_matrix function
        x_vals = [1, 2, 3]
        y_vals = [1, 4, 9]
        A, b, solution = cubic_spline_matrix(x_vals, y_vals)
        print(f"Test Cubic Spline Matrix Solution: {solution}")  # Print the result
        

if __name__ == '__main__':
    unittest.main()
