import matplotlib.pyplot as pp
import numpy as np
import sympy as sp

def graph_line(func):
    # take the values at the 2 limits
    # the line will extend until those 2 points
    x_values = np.array([x_bottom - 1, x_top + 1])

    # take the y values of the line at the 2 points
    y_values = func(x_values)

    # check if the result is not an array
    # occurs when func is a constant function
    if type(y_values) != np.ndarray:
        y_values = np.full((x_top - x_bottom, 1), y_values)

    # plot the line connecting the 2 points
    pp.plot(x_values, y_values)

# upper and lower limits for x values
x_bottom = -3
x_top = 3

# limit for x and y axes when displayed
# (can zoom and move around in the graph window so kinda irrelevant)
pp.xlim(-2, 2)
pp.ylim(-2, 2)

x = sp.Symbol('x')

# input functions
# multiple functions work to represent functions of both x and y
# e.g. for a x^2 + y^2 = 1 put [sqrt(1 - x^2), -sqrt(1 - x^2)] to plot both sides
# for y = f(x) functions just put the function in the list
functions = [x*x*x]
for function in functions:
    dx = sp.diff(function)  # derivative of input function

    # lambdified functions
    # to make functions callable
    f = sp.lambdify(x, function)
    f_prime = sp.lambdify(x, dx)

    # number of lines between each point
    lines = 25

    # take the set of integers in [x_bottom * lines, x_top * lines]
    # scale it down by lines to get the integers in that range
    # with (lines) points in between each integer point
    for x0 in [i/lines for i in range(x_bottom * lines, (x_top+1) * lines)]:
        # all lines are of the form
        # y = m(x - x0) + y0
        # where the line is a tangent to the point (x0, y0) on the curve

        # compute gradient at the point
        m = f_prime(x0)
        # equation of line
        eqn = m * (x - x0) + f(x0)
        line = sp.lambdify(x, eqn)

        # graph the line
        graph_line(line)

# add grid and show
pp.gca().set_aspect('equal', adjustable='box')
pp.grid()
pp.show()



