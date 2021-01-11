import numpy as np
import matplotlib.pyplot as plt


class Function:
    """ a is the lower boundary b is upper boundary"""
    """f is the main function and fd is its derivative if it exists"""
    """ The x0 if ir exits is the start point of many algorithms such as fixed point algo and newton algorithm"""

    def __init__(self, a, b, func, fd=None, x0=None):
        self.a = a
        self.b = b
        self.f = func
        self.fd = fd
        self.x0 = x0
        self.iterations = 300
        self.error = 1e-10
        self.pick = b

    def plot(self):
        fig = plt.figure(figsize=(12, 8))
        ax1 = plt.subplot(1, 1, 1)
        x = np.linspace(self.a, self.b, 1000)
        ax1.plot(x, self.f(x))
        ax1.plot(x, [0] * len(x))
        ax1.legend(['y=f(x)', 'y=0'])
        plt.show()

    def export(self):
        return self.a, self.b, self.f, self.fd, self.x0
