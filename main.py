class Solver:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.tolerance = 0.0001
        self.max_iters = 100
        self.roots = [None]

    def get_roots(self, guess=-1):
        order = self.get_order()
        if order == 0:
            self.zero_order_root()
        else:
            self.get_newton_root(guess)

    def zero_order_root(self):
        if self.coefficients[0] == 0:
            self.roots = ["all"]
        else:
            self.roots = ["undefined"]

    def get_order(self):
        index = 0
        for i in range(0, len(self.coefficients)):
            if self.coefficients[i] != 0:
                index = i
        return index

    def get_function(self, x):
        y_out = 0.0
        for i in range(0, len(self.coefficients)):
            y_out += self.coefficients[i] * (x ** i)
        return y_out

    def get_derivative(self, x):
        y_out = 0.0
        for i in range(0, len(self.coefficients)):
            if self.coefficients[i] != 0:
                y_out += self.coefficients[i] * i * (x ** (i - 1))
        return y_out

    def get_newton_root(self, guess):
        x = guess
        count = 0
        while count < self.max_iters:
            if abs(self.get_function(x)) < self.tolerance:
                self.roots = [x]
                break
            x = x - self.get_function(x) / self.get_derivative(x)
            count += 1
