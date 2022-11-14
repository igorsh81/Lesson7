# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.


class Cell:

    def __init__(self, cell_count: int = 1):
        self.cell_count = cell_count

    def __add__(self, other):
        return self.cell_count + other.cell_count

    def __sub__(self, other):
        if (self.cell_count - other.cell_count) < 0:
            return f'Ошибка операции: разница имеет отрицательный результат.'
        else:
            return self.cell_count - other.cell_count

    def __mul__(self, other):
        return self.cell_count * other.cell_count

    def __truediv__(self, other):
        return self.cell_count // other.cell_count

    def make_order(self, cells_in_row: int):
        master = self.cell_count // cells_in_row
        slave = self.cell_count % cells_in_row
        result = ('*' * cells_in_row + '\n') * master + '*' * slave + '\n'
        return result

''' Определение клеток'''
A = Cell(14)
B = Cell(12)

''' Операции с клетками'''
C = A + B
D1 = A - B
D2 = B - A
E = A * B
F = A / B

print(f'Сложениe: {C}')
print(f'Вычитание А-В: {D1}')
print(f'Вычитание В-А: {D2}')
print(f'Умножение: {E}')
print(f'Деление целочисленное: {F}')
print('\n--- Печать ---')
print(A.make_order(5))
print(B.make_order(5))
