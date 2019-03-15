class Solver:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.roots = []
        self.tolerance = 0.0001
        self.max_iters = 100

    def get_order(self):
        index = 0
        for i in range(0, len(self.coefficients)):
            if self.coefficients[i] != 0:
                index = i
        return index

    def get_roots(self):
        order = self.get_order()
        if order == 0:
            self.zero_get_roots()
        elif order == 1:
            self.first_get_roots()
        else:
            self.get_higher_roots()

    def zero_get_roots(self):
        if self.coefficients[0] == 0:
            self.roots = ["all"]
        else:
            self.roots = ["undefined"]

    def first_get_roots(self):
        self.roots = [-self.coefficients[0] / self.coefficients[1]]

    def get_function(self, x):
        y_out = 0.0
        for i in range(0, len(self.coefficients)):
            y_out += self.coefficients[i] * (x ** i)
        return y_out

    def get_derivative(self, x):
        y_out = 0.0
        for i in range(1, len(self.coefficients)):
            if self.coefficients[i] != 0:
                y_out += self.coefficients[i] * i * (x ** (i - 1))
        return y_out

    def get_newton_root(self, guess):
        x = guess
        count = 0
        while count < self.max_iters:
            if abs(self.get_function(x)) < self.tolerance:
                return x
            x = x - self.get_function(x) / self.get_derivative(x)
            count += 1
        return None

    def get_higher_roots(self):
        guesses = [-100, -10, -1, 1, 10, 100]
        potential_roots = []
        for g in guesses:
            potential_root = self.get_newton_root(g)
            if not potential_root:
                continue
            else:
                new_r = True
                for r in potential_roots:
                    if (1 + self.tolerance) > (potential_root / r) > 1 / (1 + self.tolerance):
                        new_r = False
                        break
                if new_r:
                    potential_roots.append(potential_root)
        self.roots = potential_roots
