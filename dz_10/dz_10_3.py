class Cell:
    def __init__(self, param):
        self.param = param

    def make_order(self, line):
        return '\n'.join(['@' * line for _ in range(self.param // line)]) + '\n' + '@' * (self.param % line)

    def __add__(self, other):
        print('Сумма ')
        return Cell(self.param + other.param)

    def __sub__(self, other):
        print('Разность ')
        return Cell(self.param - other.param) if self.param - other.param > 0 \
            else 'Вычитание невозможно, ячеек в первой клетке меньше второй'

    def __mul__(self, other):
        print('Произведение ')
        return Cell(self.param * other.param)

    def __floordiv__(self, other):
        print('Частное ')
        return Cell(self.param // other.param)

    def __str__(self):
        return f'{self.param}'


a = Cell(5)
b = Cell(25)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(b.make_order(6))
