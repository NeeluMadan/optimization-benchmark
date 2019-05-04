"""This is a module containing a test of the gradient method."""

import numpy as np
from optimizers import StupidGradientDescent
from functions import RosenBrock

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')

BUDGET = 1000

print("here")
if __name__ == "__main__":
    print("here")
    # initialize the benchmark function object
    fr = RosenBrock()
    # this is making sure it is deterministic randomness
    np.random.seed(seed=42)
    # initialize optimization algorithm object
    initstate = 10*(np.random.rand(2, 1)-1)[:, 0]
    gd = StupidGradientDescent(0.0001, initstate, fr.grad)

    # numpy array for logging
    performance = np.zeros((BUDGET,))

    for i in range(BUDGET):
        # take a gradient step with constant alpha
        gd.step()
        # save f value
        performance[i] = fr.eval(gd.state[0], gd.state[1])

    print("here")
    plt.plot(np.log10(performance))
    print("after plot")
    plt.show()
    plt.savefig("rosenbrock.png", dpi=200)