import numpy as np

def gradient_descent(g, x0, learn_rate, iterations, tolerance
                     ):
    vector = start
    for _ in range(iterations):
        diff = -learn_rate * gradient(vector)
        if np.all(np.abs(diff) <= tolerance or iterations > 100):
            break
        vector += diff
    return vector