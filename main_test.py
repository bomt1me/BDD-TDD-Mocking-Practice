import unittest
from main import *
from unittest.mock import MagicMock, Mock


class TestSolver(unittest.TestCase):
    def test_zero_order_root(self):
        params = [[0], [4]]
        expected = ["all", "undefined"]

        for i in range(0, len(expected)):
            solver = Solver(params[i])
            solver.zero_order_root()
            self.assertEqual(solver.roots[0], expected[i], "Get roots error")

    def test_get_order(self):
        params = [[0], [0, 1], [-1, 1, 1, 1]]
        expected = [0, 1, 3]

        for i in range(0, len(expected)):
            solver = Solver(params[i])
            result = solver.get_order()
            self.assertEquals(result, expected[i], "Order failed")

    def test_get_roots_zero_path(self):
        solver = Solver([0])
        solver.get_order = MagicMock(return_value=0)
        solver.zero_order_root = Mock()
        solver.get_roots()
        solver.zero_order_root.assert_called_once()

    def test_get_roots_higher_order_path(self):
        solver = Solver([1, 2, 3])
        solver.get_order = MagicMock(return_value=2)
        solver.get_newton_root = Mock()
        solver.get_roots()
        solver.get_newton_root.assert_called_once()

    def test_get_function(self):
        x_val = 1
        params = [[1, 2], [0, 2, 2]]
        expected = [3, 4]

        for i in range(0, len(expected)):
            solver = Solver(params[i])
            result = solver.get_function(x_val)
            self.assertEquals(result, expected[i], "Error function")

    def test_get_derivative(self):
        x_val = 1
        params = [[1, 2], [0, 2, 2]]
        expected = [2, 6]

        for i in range(0, len(expected)):
            solver = Solver(params[i])
            result = solver.get_derivative(x_val)
            self.assertEquals(result, expected[i], "Error deriv")


if __name__ == "__main__":
    unittest.main()
