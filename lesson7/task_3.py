class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return str(self.cells)

    def __add__(self, other):
        return 'Sum of cells is' + str(self.cells + other.cells)

    def __sub__(self, other):
        return self.cells - other.cells if self.cells - other.cells > 0 \
            else 'Unable to subtract. The quantity of sell should be the same'

    def __mul__(self, other):
        return 'Multiply of cells is' + str(self.cells * other.cells)

    def __truediv__(self, other):
        return 'Truediv of cells is' + str(round(self.cells / other.cells))

    def make_order(self, line):
        return '\n'.join(['*' * line for _ in range(self.cells // line)]) + '\n' + '*' * (self.cells % line)


a = Cell(14)
b = Cell(12)

print(a)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b.make_order(13))
