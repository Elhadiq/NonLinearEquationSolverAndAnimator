import numpy as np
from matplotlib import pyplot as plt
from model import NonLinearEquationSolver as nle
from matplotlib import animation


class Animation:

    def __init__(self, function, message="Animation de la methode de la secante", type='r'):
        self.function = function
        self.x = np.linspace(function.a, function.b, 1000)
        self.fig = plt.figure(figsize=(12, 8))
        self.ax = plt.subplot(1, 1, 1)
        self.ax.set_xlim((function.a, function.b))
        # ax1.set_ylim((min(f(a), f(b)), max(f(a), f(b))))
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.line1, = self.ax.plot(self.x, function.f(self.x), 'b', lw=2)
        self.line2, = self.ax.plot(self.x, [0] * len(self.x), 'r', lw=2) if type == 'r' else self.ax.plot(self.x,
                                                                                                          self.x, 'r',
                                                                                                          lw=2)
        self.lignes, = self.ax.plot([], [], '')
        self.pt, = self.ax.plot([], [], 'ro', ms=10)
        self.txt_title = self.ax.set_title(message)
        self.ax.legend(['y=f(x)', 'y=0'])
        if type == 'r':
            self.xn_secante = nle.generate_values(nle.secante(function), function.error, function.iterations)
            self.xn_newton = nle.generate_values(nle.newton(function), function.error, function.iterations)
            self.xn_bisect = nle.generate_values(nle.dichotomie(function), function.error, function.iterations)
        else:
            self.x_ptfixe = nle.generate_values(nle.point_fixe(function), function.error, function.iterations)

    # TODO anime le secante

    def animer_la_secante(self, n):
        pick = self.function.pick
        if n == 0:
            self.ax.plot(self.function.a, self.function.f(self.function.a), 'ro')
            self.ax.plot(self.function.b, self.function.f(self.function.b), 'ro')
            self.ax.plot([self.function.a, self.function.b],
                         [self.function.f(self.function.a), self.function.f(self.function.b)], '--')
        else:
            self.ax.plot([self.xn_secante[n - 1], self.function.pick],
                         [self.function.f(self.xn_secante[n - 1]), self.function.f(self.function.pick)], '--')
            self.pt.set_data(self.xn_secante[:n], [0] * n)
            self.ax.plot([self.xn_secante[n - 1], self.xn_secante[n - 1]], [0, self.function.f(self.xn_secante[n - 1])],
                         '--')
        txt_title = self.ax.set_title('Méthode de la secante: frame {}'.format(n))
        return self.line1, self.line2
