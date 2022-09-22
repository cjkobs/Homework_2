from scipy.optimize import minimize
import numpy as np

# This section is part a
# function, fun, that we want to solve for(minimize)
fun = lambda x: (x[0] + 1) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2
# initial guess since that is necessary to start
xinit = [-1, 0, 1]
# constraints based on solving the form given
constr = ({"type": "eq", "fun": lambda x: x[0] + 2 * x[1] + 3 * x[2] - 1})
# no bounds to be set for the problem
res = minimize(fun, xinit, method='SLSQP', constraints=constr)
# print the answer
print(res.x)

# This section is part b, pretty sure this is what it's asking for
fun = lambda x: (2 - 2 * x[0] - 3 * x[1]) ** 2 + (x[0]) ** 2 + (x[1] - 1) ** 2
print(fun)
# god how did it take me this long to just hardcode the gradient in, whatever here are the gradient and hessian
grad = lambda x: [(-8 + 10 * x[0] + 12 * x[1]), (-14 + 12 * x[1] + 20 * x[2])]
print(grad)
gradt = grad.transpose(grad)
print(gradt)
hess = [[10, 12], [12, 20]]
print(hess)

t = 0.5
def phi(x, alph):
    return fun - (t * np.matmul(gradt, grad) * alph)
def new_alph(x):
    alph = 1
    k = 0
    while fun(x - alph * grad) > phi(x,alph) and k < 100:
        alph = 0.5* alph
        k = k + 1
    return alph
