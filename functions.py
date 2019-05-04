""" 
This is the module containing function and their gradinet
"""

import numpy as np


class RosenBrock:

    def __init__(self, a=1., b=100.):
        self.a = a
        self.b = b

    def eval(self, x, y):
        return (self.a-x)**2 + self.b*(y-x**2)**2

    def grad(self, x, y):
        return np.array([-2.*(self.a-x), 0.]) + 2.*self.b*(y-x**2.)*np.array([-2.*x, 1.])