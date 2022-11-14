# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

def my_f(my_list):
    if len(my_list[0]) == 2:
        matrix = ('\n'.join("{:4} {:4}".format(v1, v2) for v1, v2 in my_list))
    if len(my_list[0]) == 3:
        matrix = ('\n'.join("{:4} {:4} {:4}".format(v1, v2, v3) for v1, v2, v3 in my_list))
    if len(my_list[0]) == 4:
        matrix = ('\n'.join("{:4} {:4} {:4} {:4}".format(v1, v2, v3, v4) for v1, v2, v3, v4 in my_list))
    return matrix


class Matrix:
    def __init__(self, *args):
        self.args = args[0]

    def __str__(self):
        matrix = my_f(self.args)
        return matrix

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.args)):
            temp = []
            for n in range(len(self.args[i])):
                temp.append(self.args[i][n] + other[i][n])
            new_matrix.append(temp)
            matrix = my_f(new_matrix)
        return matrix


matr_1 = [[31, 22], [37, 43], [51, 86]]
matr_1_1 = [[100, 2], [307, 543], [521, 186]]
matr_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
matr_2_1 = [[35, 54, 132], [24, 74, 86], [-18, 684, -98]]
matr_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
matr_3_1 = [[783, 58, 89, 37], [88, 378, 57, 145]]

matrix_1 = Matrix(matr_1)
print(f'Matrix1:')
print(matrix_1)

print()
matrix_1 = Matrix(matr_1_1)
print(f'Matrix1.1:')
print(matrix_1)

print()
print(f'Matrix1 + Matrix1.1:')
print(matrix_1 + matr_1)

print('\n' * 2)
matrix_1 = Matrix(matr_2)
print(f'Matrix2:')
print(matrix_1)

print()
matrix_1 = Matrix(matr_2_1)
print(f'Matrix2.1:')
print(matrix_1)

print()
print(f'Matrix2 + Matrix2.1:')
print(matrix_1 + matr_2)

print('\n' * 2)
matrix_1 = Matrix(matr_3)
print(f'Matrix3:')
print(matrix_1)

print()
matrix_1 = Matrix(matr_3_1)
print(f'Matrix3.1:')
print(matrix_1)

print()
print(f'Matrix3 + Matrix3.1:')
print(matrix_1 + matr_3)
