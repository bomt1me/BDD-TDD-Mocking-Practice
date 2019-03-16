from behave import *
from main import *


@given(u'a function {function}')
def step_impl(context, function):
    function = [float(i) for i in function.split(',')]
    context.solver = Solver(function)


@when(u'asked to find roots')
def step_impl(context):
    context.solver.get_roots()


@then(u'the roots are {roots}')
def step_impl(context, roots):
    if roots == "all":
        roots = ["all"]
        assert (context.solver.roots == roots)
    elif roots == "undefined":
        roots = ["undefined"]
        assert (context.solver.roots == roots)
    else:
        roots = [float(i) for i in roots.split(',')]
        assert ((1 + 0.0001) > (context.solver.roots[0] / roots[0]) > 1 / (1 + 0.0001))


@when(u'asked to find roots for a guess {guess}')
def step_impl(context, guess):
    guess = float(guess)
    context.solver.get_roots(guess)
