from models.base_model import base_model


def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


class FiniteFieldElt:
    def __init__(self, p, x):
        self.p = p
        self.x = x % self.p
        self.reducing = [1, 0]

    def __pow__(self, power, modulo=None):
        return FiniteFieldElt(self.p, pow(self.x, power.x))

    def __add__(self, other):
        return FiniteFieldElt(self.p, (self.x + other.x) % self.p)

    def __sub__(self, other):
        return FiniteFieldElt(self.p, (self.x - other.x) % self.p)

    def __mul__(self, other):
        return FiniteFieldElt(self.p, (self.x * other.x) % self.p)

    def __neg__(self):
        return FiniteFieldElt(self.p, - self.x)

    def __floordiv__(self, other):
        pass

    def __truediv__(self, other):
        return self * other.inv()

    def inv(self):
        g, x, _ = xgcd(self.x, self.p)
        if g == 1:
            return FiniteFieldElt(self.p, x)

    def __eq__(self, other):
        return self.x == other.x

    def __le__(self, other):
        return self.x <= other.x

    def __lt__(self, other):
        return self.x < other.x

    def __ge__(self, other):
        return self.x >= other.x

    def __gt__(self, other):
        return self.x > other.x

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return str(self.x)


class FiniteSet:
    def __init__(self, p):
        self.p = p

    def __iter__(self):
        return FiniteSetIterator(self.p)


class FiniteSetIterator:
    def __init__(self, p):
        self.p = p
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current == self.p:
            raise StopIteration
        return FiniteFieldElt(self.p, self.current)


class model(base_model):
    def __init__(self, Z=None):
        super().__init__()

        if Z:
            self.p = int(Z[2:-1])
        else:
            self.p = 5

        E = FiniteSet(self.p)
        self._value_set = dict({'E': E}, **self.bool_values)

    def constante(self, x):
        return FiniteFieldElt(self.p, x)
