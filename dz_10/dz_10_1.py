class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('  '.join(map(str, n)) for n in self.matrix)

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                       range(len(self.matrix))])


matrix_1 = Matrix([[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]])
matrix_2 = Matrix([[9, 8, 7, 2], [6, 5, 4, 2], [3, 2, 1, 2]])
matrix_3 = Matrix([[1, 2, 3, -3], [4, 5, 6, 3], [7, 8, 9, -3]])
print(matrix_1)
print('-' * 10)
print(matrix_2)
print('-' * 10)
print(matrix_3)
print('-' * 10)
print(matrix_1 + matrix_2)
print('-' * 10)
print(matrix_1 + matrix_2 + matrix_3)
