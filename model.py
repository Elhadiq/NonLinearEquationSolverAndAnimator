from functions import Function


class NonLinearEquationSolver:
    @staticmethod
    def dichotomie(function):

        x = function.a
        y = function.b
        while True:
            mid = (x + y) / 2
            yield mid
            if function.f(mid) == 0:
                break
            if function.f(x) * function.f(mid) <= 0:
                y = mid
            else:
                x = mid

    @staticmethod
    def point_fixe(function):
        x1 = function.x0
        while True:
            x1 = function.f(x1)
            yield x1
            if x1 == function.f(x1):
                break

    @staticmethod
    def secante(function):
        x0 = function.a
        x1 = function.b
        while True:
            x2 = (x1 * function.f(x0) - x0 * function.f(x1)) / (function.f(x0) - function.f(x1))
            yield x2
            if function.f(x2) * function.f(x0) <= 0:
                x1 = x2
            else:
                x0 = x2
            if function.f(x2) == 0:
                break

    @staticmethod
    def newton(function):
        g = Function(function.a, function.b, lambda x: x - function.f(x) / function.fd(x), None, function.x0)
        gen = NonLinearEquationSolver.point_fixe(g)
        while True:
            nt = next(gen)
            yield nt
            if nt == 0:
                break

    @staticmethod
    def generate_values(gen, error, number_of_iterations):
        """The generator will ends in tree cases
        case 1: if we reached the solution we want ie f(x)=0 or f(x)=x
        case 2: if we passe number_of_iterations
        case 3: if we reached the errors wanted
        """
        x = [next(gen)]
        for i in range(number_of_iterations):
            try:
                x.append(next(gen))
                assert abs(x[-2] - x[-1]) > error
            except:
                break
        return x
