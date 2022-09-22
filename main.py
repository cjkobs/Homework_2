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
gradt = lambda x: [[-8 + 10 * x[0] + 12 * x[1]], [-14 + 12 * x[1] + 20 * x[2]]]
print(gradt)
hess = [[10, 12], [12, 20]]
print(hess)

# setting up the algorithm that was discussed in class when doing inexact line search
# chose 0.5 since it's case dependent and it was right in the middle
t = 0.5
x_val=[]
def phi(x, alph):
    return fun - (t * np.matmul(gradt, grad) * alph)
def new_alph(x):
    alph = 1
    k = 0
    while fun(x - alph * grad) > phi(x, alph) and k < 100:
        alph = 0.5 * alph
        k = k + 1
    return alph
# I tried adding an else break condition at the end but it was a pain, gonna ask my CS buddy if he knows how

# So what I was trying to do was define my minimization function, the gradient of that function and the hessian
# from there, I made the functions that we talked about in lecture 7 while going through the inexact line search
# The problem is I'm not sure what to do with them especially since it won't let me print new_alph
# I'm guessing it's because it's a function and not a variable in which case it would need initial conditions?
# That's above my pay grade, hopefully the code for how to do a simple problem like this will be posted so I can
# hopefully get better at coding for the future.

# I tried some stuff but coding just sucks the life out of me
# unless it's in MATLAB and then it's iffy
# I'll attach this git link to my answers but I'm tired and don't see how I can
# get a solution with 4 hours left with little knowledge of how coding works
# I'm looking forward to the exam because I feel like I understand
# the material better conceptually than I am able to code it. It's all greek to me

