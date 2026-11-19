
# Brandon Jun // COMSC 078 // Trees & Dictionaries

from abc import ABC, abstractmethod
from fractions import Fraction


class GenericMatrix(ABC):

    def __init__(self, matrix):
        self._matrix = matrix

    def getRows(self):
        return self._matrix

    # ----- Abstract element-level methods (overridden in subclasses) -----

    @abstractmethod
    def __add__(self, a, b):
        pass

    @abstractmethod
    def __mul__(self, a, b):
        pass

    @abstractmethod
    def __zero__(self):
        pass

    def __addMatrix__(self, other):
        rows = len(self._matrix)
        cols = len(self._matrix[0])
        if rows != len(other._matrix) or cols != len(other._matrix[0]):
            raise ValueError("Matrices must have the same dimensions to be added.")

        result = []
        for i in range(rows):
            new_row = []
            for j in range(cols):
                new_row.append(self.__add__(self._matrix[i][j], other._matrix[i][j]))
            result.append(new_row)
        return type(self)(result)

    def __multiplyMatrix__(self, other):
        n = len(self._matrix[0])
        if n != len(other._matrix):
            raise ValueError("Columns of the first matrix must equal rows of the second.")

        result = []
        for i in range(len(self._matrix)):
            new_row = []
            for j in range(len(other._matrix[0])):
                total = self.__zero__()
                for k in range(n):
                    product = self.__mul__(self._matrix[i][k], other._matrix[k][j])
                    total = self.__add__(total, product)
                new_row.append(total)
            result.append(new_row)
        return type(self)(result)

    def __str__(self):
        rows = [[str(element) for element in row] for row in self._matrix]
        width = max(len(text) for row in rows for text in row)
        lines = []
        for row in rows:
            lines.append("   ".join(text.rjust(width) for text in row))
        return "\n".join(lines)


class IntegerMatrix(GenericMatrix):

    def __init__(self, matrix):
        super().__init__(matrix)

    def __add__(self, a, b):
        return a + b

    def __mul__(self, a, b):
        return a * b

    def __zero__(self):
        return 0


class RationalMatrix(GenericMatrix):

    def __init__(self, matrix):
        super().__init__(matrix)

    def __add__(self, a, b):
        numerator = a.numerator * b.denominator + b.numerator * a.denominator
        denominator = a.denominator * b.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, a, b):
        return Fraction(a.numerator * b.numerator, a.denominator * b.denominator)

    def __zero__(self):
        return Fraction(0, 1)


def show_operation(a, symbol, b, c):

    grids = [[[str(x) for x in row] for row in m.getRows()] for m in (a, b, c)]
    width = max(len(text) for grid in grids for row in grid for text in row)
    middle = len(grids[0]) // 2

    for i in range(len(grids[0])):
        parts = ["   ".join(text.rjust(width) for text in grid[i]) for grid in grids]
        op = symbol if i == middle else " "
        eq = "=" if i == middle else " "
        print(parts[0] + "   " + op + "   " + parts[1] + "   " + eq + "   " + parts[2])


def main():

    m1 = IntegerMatrix([[1, 2, 3],
                        [4, 5, 6],
                        [1, 1, 1]])
    m2 = IntegerMatrix([[1, 1, 1],
                        [2, 2, 2],
                        [0, 0, 0]])

    print("m1 + m2 is")
    show_operation(m1, "+", m2, m1.__addMatrix__(m2))
    print()
    print("m1 * m2 is")
    show_operation(m1, "*", m2, m1.__multiplyMatrix__(m2))
    print()

    r1 = RationalMatrix([[Fraction(1, 5), Fraction(1, 6), Fraction(1, 7)],
                         [Fraction(2, 5), Fraction(1, 3), Fraction(2, 7)],
                         [Fraction(3, 5), Fraction(1, 2), Fraction(3, 7)]])
    r2 = RationalMatrix([[Fraction(1, 6), Fraction(1, 7), Fraction(1, 8)],
                         [Fraction(1, 3), Fraction(2, 7), Fraction(1, 4)],
                         [Fraction(1, 2), Fraction(3, 7), Fraction(3, 8)]])

    print("m1 + m2 is")
    show_operation(r1, "+", r2, r1.__addMatrix__(r2))
    print()
    print("m1 * m2 is")
    show_operation(r1, "*", r2, r1.__multiplyMatrix__(r2))


main()