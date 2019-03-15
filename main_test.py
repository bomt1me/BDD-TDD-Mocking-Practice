import unittest
from main import *
from unittest.mock import MagicMock, Mock


class TestSolver(unittest.TestCase):
    def test_get_order(self):
        params = [[0], [4], [1, 1], [0, 1, 0, 1], [0, 0, 1], [1, 0, 0], [0, 0]]
        expected = [0, 0, 1, 3, 2, 0, 0]

        for iteration in range(0, len(params)):
            solver = Solver(params[iteration])
            result = solver.get_order()
            self.assertEquals(result, expected[iteration],
                              "Order is not correct for iteration {0}".format(iteration))

    def test_get_roots_zero_is_called(self):
        solver = Solver([2])
        solver.get_order = MagicMock(return_value=0)
        solver.zero_get_roots = Mock()
        solver.get_roots()
        solver.zero_get_roots.assert_called_once()

    def test_get_roots_first_is_called(self):
        solver = Solver([2, 2])
        solver.get_order = MagicMock(return_value=1)
        solver.first_get_roots = Mock()
        solver.get_roots()
        solver.first_get_roots.assert_called_once()

    def test_get_roots_higher_is_called(self):
        solver = Solver([2, 2, 2])
        solver.get_order = MagicMock(return_value=2)
        solver.get_higher_roots = Mock()
        solver.get_roots()
        solver.get_higher_roots.assert_called_once()

    def test_zero_get_roots(self):
        params = [[0], [4], [0, 0], [1, 0]]
        expected = [["all"], ["undefined"], ["all"], ["undefined"]]

        for iteration in range(0, len(params)):
            solver = Solver(params[iteration])
            solver.zero_get_roots()
            self.assertEquals(solver.roots, expected[iteration],
                              "Roots not correct for iteration {0}".format(iteration))

    def test_first_get_roots(self):
        params = [[0, 1], [2, 4], [-3, 12]]
        expected = [[0], [-0.5], [1/4]]

        for iteration in range(0, len(params)):
            solver = Solver(params[iteration])
            solver.first_get_roots()
            self.assertEquals(solver.roots, expected[iteration],
                              "Roots not correct for iteration {0}".format(iteration))

    def test_get_function(self):
        x_val = 2
        params = [[0, 1, 4], [2, 4, 2], [-3, 12], [1], [4, 0]]
        expected = [18, 18, 21, 1, 4]

        for iteration in range(0, len(params)):
            solver = Solver(params[iteration])
            result = solver.get_function(x_val)
            self.assertEquals(result, expected[iteration],
                              "FunctionValue not correct for iteration {0}".format(iteration))

    def test_get_derivative(self):
        x_val = 2
        params = [[0, 1, 4], [2, 4, 2], [-3, 12], [1], [4, 0]]
        expected = [17, 12, 12, 0, 0]

        for iteration in range(0, len(params)):
            solver = Solver(params[iteration])
            result = solver.get_derivative(x_val)
            self.assertEquals(result, expected[iteration],
                              "DerivativeValue not correct for iteration {0}".format(iteration))

    def test_get_newton_root(self):
        params = [[-2, -3/2, 3/4, 1/4]]
        expected = [[-4, -1, 2]]
        guesses = [-10, -1, 1]

        for i in range(0, len(expected)):
            for j in range(0, len(expected[i])):
                solver = Solver(params[i])
                r = solver.get_newton_root(guesses[j])
                self.assertAlmostEqual(r, expected[i][j], 4, "Values not correct for i {0}".format(i))

    def test_get_higher_roots(self):
        params = [[1, 2, 3, 4], [5, -2, 0, -4], [-2, -3/2, 3/4, 1/4]]
        expected = [[-0.60583], [0.92371], [-4, -1, 2]]

        for iteration in range(0, len(params)):
            solver = Solver(params[iteration])
            solver.get_higher_roots()
            for _, r in enumerate(solver.roots):
                self.assertAlmostEqual(r, expected[iteration][_], 4,
                                       "Value not correct for iteration {0}".format(iteration))


if __name__ == "__main__":
    unittest.main()
