from sympy import *

# Derivative
# function to calculate derivative of math
def basic_derivative(formula):
    x = Symbol('x')
    formula = eval(formula)
    derivative_f = formula.diff(x)
    data = {
        "status": "ok",
        "formula": latex(formula),
        "result": latex(derivative_f),
        "msg": "no_error"
    }
    return data

# Quadratic Equation
# function to calculate quadratic equation of math
def quadratic_equation(formula):
    x = Symbol('x')
    formula = eval(formula)
    roots = solve(formula, x, dict=False)
    data = {
        "status": "ok",
        "formula": latex(formula),
        "x": [
            latex(roots[0]),
            latex(roots[1])
        ],
        "msg": "quadratic_equation"
    }
    return data