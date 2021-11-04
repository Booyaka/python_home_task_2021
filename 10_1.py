class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))  # Отображение стырил =С

    def __add__(self, other):
        return Matrix([map(sum, zip(*i))
                       for i in zip(self.matrix, other.matrix)])


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1 + matrix_2)