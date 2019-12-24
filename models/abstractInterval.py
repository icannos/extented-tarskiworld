
from abstract import *
from parsers.logicParser import logicParser

class AbstractInterval:
    def __init__(self, b):
        self.value = None

        if isinstance(b, Bottom):
            self.value = b

        elif isinstance(b, int):
            self.value = (b, b)
        elif isinstance(b, str):
            self.value = (b,b)

        elif isinstance(b, tuple):
            self.value = b
        if isinstance(b, Top):
            self.value = (float("-inf"), float("inf"))

    def __contains__(self, x):
        return self.contains(x)

    def contains(self, x):
        v = AbstractInterval(x)

        return not self.disjoint_from(v)

    def __repr__(self):
        if self.value is not Bottom():
            return "<Interval [" + str(self.value[0]) + ", " + str(self.value[1]) + "]>"
        else:
            return "<Interval " + str(self.value) + ">"

    def __str__(self):
        if self.value is not Bottom():
            return "<Interval [" + str(self.value[0]) + ", " + str(self.value[1]) + "]>"
        else:
            return "<Interval " + str(self.value) + ">"

    def __eq__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return None

        a1 = self.value[0]
        b1 = self.value[1]

        a2 = other.value[0]
        b2 = other.value[1]

        if a1 == b1 and b1 == a2 and a2 == b2:
            return True
        elif self.disjoint_from(other):
            return False
        else:
            return None

    def __ne__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return None

        return self.disjoint_from(other)

    def __le__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return None

        return self.value[1] <= other.value[0]

    def __lt__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return None

        if not self.disjoint_from(other):
            return None

        return self.value[1] < other.value[0]

    def __ge__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return None

        return self.value[0] >= other.value[1]

    def __gt__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return None

        if not self.disjoint_from(other):
            return None

        return self.value[0] > other.value[1]

    def __add__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return AbstractInterval(Bottom())

        a1 = self.value[0]
        b1 = self.value[1]

        a2 = other.value[0]
        b2 = other.value[1]

        return AbstractInterval((a1 + a2, b1 + b2))

    def __mul__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return AbstractInterval(Bottom())

        a1 = self.value[0]
        b1 = self.value[1]

        a2 = other.value[0]
        b2 = other.value[1]

        return AbstractInterval((a1 * a2, b1 * b2))

    def __sub__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return AbstractInterval(Bottom())

        a1 = self.value[0]
        b1 = self.value[1]

        a2 = other.value[0]
        b2 = other.value[1]

        return AbstractInterval((a1 - b2, b1 - a2))

    def __truediv__(self, other):
        if self.value == Bottom() or other.value == Bottom():
            return AbstractInterval(Bottom())

        a1 = self.value[0]
        b1 = self.value[1]

        a2 = other.value[0]
        b2 = other.value[1]

        if a2 == 0:
            a2 = a2 - 1
        if b2 == 0:
            b1 = b1 + 1

        return AbstractInterval((a1 / b2, b1 / a2))

    def __pow__(self, power, modulo=None):
        if self.value == Bottom() or power.value == Bottom():
            return AbstractInterval(Bottom())

        a1 = self.value[0]
        b1 = self.value[1]

        a2 = power.value[0]
        b2 = power.value[1]

        if a1 == 0:
            a1 = a1 - 1
        if a2 != 0:
            a2 = a2 + 1

        return AbstractInterval((a1 ** a2, b1 ** b2))

    def __neg__(self):
        if self.value == Bottom():
            return AbstractInterval(Bottom())

        a, b = self.value[0], self.value[1]
        return AbstractInterval((-b, -a))

    def disjoint_from(self, other):
        if self.value == Bottom():
            return None
        if other.value == Bottom():
            return None

        if other.value[0] <= self.value[1] <= other.value[1]:
            return False
        if other.value[0] <= self.value[0] <= other.value[1]:
            return False

        if self.value[0] <= other.value[1] <= self.value[1]:
            return False
        if self.value[0] <= other.value[0] <= self.value[1]:
            return False

        return True

    def sup(self, other):
        if self.value == Bottom():
            return AbstractInterval(other.value)
        if other.value == Bottom():
            return AbstractInterval(self.value)

        return AbstractInterval((min(self.value[0], other.value[0]), max(self.value[1], other.value[1])))

    def inf(self, other):
        if self.value == Bottom():
            return AbstractInterval(other.value)
        if other.value == Bottom():
            return AbstractInterval(self.value)

        return AbstractInterval((max(self.value[0], other.value[0]), min(self.value[1], other.value[1])))

    @staticmethod
    def random(a, b):
        if a.value == Bottom() or b.value == Bottom():
            return AbstractInterval(Bottom())

        a1, b1 = a.value[0], a.value[1]
        a2, b2 = b.value[0], b.value[1]

        return AbstractInterval((min(a1, a2), max(b1, b2)))

    @staticmethod
    def deduce_from_comp(op, b):
        if b.value == Bottom():
            return AbstractInterval(Bottom())

        if op == logicParser.EQ:
            return AbstractInterval(b.value)
        elif op == logicParser.NEQ:
            return AbstractInterval((float("-inf"), float("inf")))
        elif op == logicParser.LT:
            return AbstractInterval((float("-inf"), b.value[1] - 1))
        elif op == logicParser.LTEQ:
            return AbstractInterval((float("-inf"), b.value[1]))
        elif op == logicParser.GT:
            return AbstractInterval((b.value[0] + 1, float("inf")))
        elif op == logicParser.GTEQ:
            return AbstractInterval((b.value[0], float("inf")))
        else:
            return AbstractInterval((float("-inf"), float("inf")))

    def widening(self, y):
        if self.value == Bottom():
            return AbstractInterval(y.value)
        elif y.value == Bottom():
            return AbstractInterval(self.value)

        else:
            a1, b1 = self.value
            a2, b2 = y.value

            if a2 >= a1 and b2 <= b1:
                return AbstractInterval((a1, b1))
            elif a2 >= a1 and b2 > b1:
                return AbstractInterval((a1, float("+inf")))
            elif a2 < a1 and b2 <= b1:
                return AbstractInterval((float("-inf"), b1))
            else:
                return AbstractInterval((float("-inf"), float("+inf")))


class AbstractIntervalMem(AbstractMemory):
    def __init__(self, assignment, abstractElt):
        AbstractMemory.__init__(self, assignment, abstractElt)

    @staticmethod
    def newTopElt(abstractElt):
        def f():
            return abstractElt((float("-inf"), float("inf")))

        return f

    def widening(self, b):
        mem = AbstractIntervalMem({}, self.abstractClass)

        for k, v in self.items():
            mem[k] = v.widening(b[k])

        return mem
