
import unittest
from assignment_3 import euler_method, runge_kutta_method

class TestAssignment3(unittest.TestCase):

    def test_func1(self):
        def func1(t, y):
            return t - y**2
        self.assertAlmostEqual(euler_method(func1, 0, 1, 0.2, 10), 1.244638, places=5)
        self.assertAlmostEqual(runge_kutta_method(func1, 0, 1, 0.2, 10), 1.251317, places=5)

    def test_func2(self):
        def func2(t, y):
            return y - t**2 + 1
        self.assertAlmostEqual(euler_method(func2, 0, 0.5, 0.2, 10), 2.48832, places=5)
        self.assertAlmostEqual(runge_kutta_method(func2, 0, 0.5, 0.2, 10), 2.71767, places=5)

    def test_func3(self):
        def func3(t, y):
            return 2*t + y
        self.assertAlmostEqual(euler_method(func3, 0, 0, 0.2, 10), 5.09328, places=5)
        self.assertAlmostEqual(runge_kutta_method(func3, 0, 0, 0.2, 10), 5.43656, places=5)

if __name__ == "__main__":
    unittest.main()
