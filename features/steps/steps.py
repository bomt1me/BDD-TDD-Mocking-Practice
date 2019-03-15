from behave import *
from main import *


@given(u'a zero order function [0]')
def step_impl(context):
    context.solver = Solver([0])


@when(u'asked to find roots')
def step_impl(context):
    context.solver.get_roots()


@then(u'the roots are ["all"]')
def step_impl(context):
    assert (context.solver.roots == ["all"])


@given(u'a zero order function [4]')
def step_impl(context):
    context.solver = Solver([4])


@then(u'the roots are ["undefined"]')
def step_impl(context):
    assert (context.solver.roots == ["undefined"])


@given(u'a first order function [0, 0]')
def step_impl(context):
    context.solver = Solver([0, 0])


@given(u'a first order function [4, 0]')
def step_impl(context):
    context.solver = Solver([4, 0])


@given(u'a first order function [0, 1]')
def step_impl(context):
    context.solver = Solver([0, 1])


@then(u'the roots are [0]')
def step_impl(context):
    assert (context.solver.roots == [0])


@given(u'a first order function [2, 4]')
def step_impl(context):
    context.solver = Solver([2, 4])


@then(u'the roots are [-0.5]')
def step_impl(context):
    assert (context.solver.roots == [-0.5])


@given(u'a first order function [-3, 12]')
def step_impl(context):
    context.solver = Solver([-3, 12])


@then(u'the roots are [1/4]')
def step_impl(context):
    context.solver = Solver([1/4])


@given(u'a greater than first order function [1, 2, 3, 4]')
def step_impl(context):
    context.solver = Solver([1, 2, 3, 4])


@then(u'the roots are [-0.60583]')
def step_impl(context):
    assert ((1.0 + 0.0001) > (context.solver.roots[0] / -0.60583) > 1.0 / (1.0 + 0.0001))


@given(u'a greater than first order function [5, -2, 0, -4]')
def step_impl(context):
    context.solver = Solver([5, -2, 0, -4])


@then(u'the roots are [0.92371]')
def step_impl(context):
    assert ((1 + 0.0001) > (context.solver.roots[0] / 0.92371) > 1 / (1 + 0.0001))


@given(u'a greater than first order function [-2, -3/2, 3/4, 1/4]')
def step_impl(context):
    context.solver = Solver([-2, -3/2, 3/4, 1/4])


@then(u'the roots are [-4, -1, 2]')
def step_impl(context):
    _roots = context.solver.roots
    _roots.sort()
    expected = [-4, -1, 2]
    assert (len(expected) == len(_roots))
    for i in range(0, len(expected)):
        assert ((1 + 0.0001) > (_roots[i] / expected[i]) > 1 / (1 + 0.0001))
