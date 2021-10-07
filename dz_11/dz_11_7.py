class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.comp_num = complex(self.num_1, self.num_2)

    def __str__(self):
        return f'Результат: {self.comp_num}'

    def __add__(self, other):
        return self.comp_num + other.comp_num

    def __mul__(self, other):
        return self.comp_num * other.comp_num


a = ComplexNumber(1, 2)
b = ComplexNumber(2, 3)

print(a + b)
print(a * b)
