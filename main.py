import numpy as np
from functions import Function
from model import NonLinearEquationSolver as nle
from animer import Animation
from matplotlib import animation
from IPython.display import HTML

f1 = Function(0, 1, lambda x: np.exp(-x ** 2 / 2) - x, lambda x: -x * np.exp(-x ** 2 / 2) - 1, 0.5)
f2 = Function(0.01, 2, lambda x: x ** 2 - x, lambda x: 2 * x, 0.5)
f3 = Function(0.1, 2, lambda x: 1 / x - 2, lambda x: -1 / (x ** 2), 0.2)
f4 = Function(0.2, 2, lambda x: 1 / x - 2, lambda x: -1 / x ** 2, 0.2)

animer = Animation(f4)

anim = animation.FuncAnimation(animer.fig, animer.animer_la_secante, frames=15, interval=1500, blit=True)
print("OK")
