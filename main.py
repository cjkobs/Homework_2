from scipy.optimize import minimize, fmin_cg
import matplotlib as plt
import numpy as np

# This section is part a
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

# This section is part b, pretty sure this is what it's asking for
fun = lambda x: (2-2*x[0]-3*x[1])**2 + (x[0])**2 + (x[1]-1)**2
# god how did it take me this long to just hardcode the gradient in, whatever here are the gradient and hessian
grad= lambda x: [(-8+10*x[0]+12*x[1]),(-14+12*x[1]+20*x[2])]
hess= [[10, 12],[12 20]]

