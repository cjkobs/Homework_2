from scipy.optimize import minimize
import numpy as np
# function, fun, that we want to solve for(minimize)
fun = lambda x: (x[0]+1)**2 + (x[1])**2 + (x[2]-1)**2
# initial guess since that is necessary to start
xinit = [-1, 0, 1]
# constraints based on solving the form given
constr = ({"type": "eq", "fun": lambda x: x[0] + 2*x[1] + 3*x[2] - 1})
# no bounds to be set for the problem
res = minimize(fun, xinit, method= 'SLSQP', constraints=constr)
# print the answer
print(res.x)