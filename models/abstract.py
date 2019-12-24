from collections import defaultdict


class AbstractElement:
    """
    Parent class to represent all our abstracts elements
    """

    def __init__(self):
        self.value = None

    def lattice_eq(self, other):
        return self.value == other.value


class FlatElement(AbstractElement):
    """
    Implement the partial order in which element are only compared to TOp et bottom and unrelated to each-other
    """

    def __init__(self, elt):
        AbstractElement.__init__(self)



    def sup(self, other):
        if isinstance(self.value, int) and isinstance(other.value, int):
            if self.value == other.value:
                return type(self)(self.value)
            else:
                return type(self)(Top())
        elif isinstance(self.value, Top) or isinstance(other.value, Top):
                return type(self)(Top())
        else:
            if isinstance(self.value, Bottom):
                return type(self)(other.value)
            else:
                return type(self)(self.value)

    def inf(self, other):
        if isinstance(self.value, int) and isinstance(other.value, int):
            if self.value == other.value:
                return type(self)(self.value)
            else:
                return type(self)(Bottom())
        elif isinstance(self.value, Bottom) or isinstance(other.value, Bottom):
            return type(self)(Bottom())

        else:
            if isinstance(self.value, Top):
                return type(self)(other.value)
            else:
                return type(self)(self.value)




class Top:
    """
    Top element, greater than anything
    """

    def __init__(self):
        pass

    def __repr__(self):
        return str('\u22A4')

    def __str__(self):
        return str('\u22A4')

    def __eq__(self, other):
        return isinstance(other, Top)

    def __le__(self, other):
        if self == other:
            return True
        else:
            return False

    def __lt__(self, other):
        return False

    def __ge__(self, other):
        return True

    def __gt__(self, other):
        if self == other:
            return False
        else:
            return True

    def __add__(self, other):
        if isinstance(other, Bottom):
            return Bottom()
        else:
            return Top()

    def __mul__(self, other):
        if isinstance(other, Bottom):
            return Bottom()
        else:
            return Top()

    def __sub__(self, other):
        if isinstance(other, Bottom):
            return Bottom()
        else:
            return Top()


class Bottom:
    """
    Bottom element, smaller than anything
    """

    def __init__(self):
        pass

    def __repr__(self):
        return str('\u22A5')

    def __str__(self):
        return str('\u22A5')

    def __eq__(self, other):
        return isinstance(other, Bottom)

    def __ge__(self, other):
        if self == other:
            return True
        else:
            return False

    def __gt__(self, other):
        return False

    def __le__(self, other):
        return True

    def __lt__(self, other):
        if self == other:
            return False
        else:
            return True

    def __add__(self, other):
        return Bottom()

    def __mul__(self, other):
        return Bottom()

    def __sub__(self, other):
        return Bottom()





class AbstractMemory(defaultdict):
    """
    Class used to represent our memory containing abstract data, has to support union, intersection and widening.
    Can be replaced by other representation for polyhedron
    """

    def __init__(self, assignment, abstractElt):
        self.abstractClass = abstractElt

        defaultdict.__init__(self, self.newTopElt(abstractElt))

        if assignment:
            for k, v in assignment.items():
                self[k] = v

    def __eq__(self, other):
        for k, v in self.items():
            if other[k].value != v.value:
                return False

        return True

    def __ne__(self, other):
        for k, v in self.items():
            if other[k].value != v.value:
                return True

        return False

    @staticmethod
    def newTopElt(abstractElt):
        def f():
            return abstractElt(Top())

        return f

    def copy(self):
        return type(self)(self, self.abstractClass)

    def union(self, other):
        m = type(self)({}, self.abstractClass)

        for k, v in self.items():
            m[k] = v.sup(other[k])

        return m

    def inter(self, other):
        m = type(self)({}, self.abstractClass)

        for k, v in self.items():
            m[k] = self[k].inf(other[k])

        return m

    def deduce_from_cond(self):
        pass

    def widening(self, b):
        return b.copy()
