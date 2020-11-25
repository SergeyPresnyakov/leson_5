# ! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31	22
37	43
51	86

3	5	32
2	4	6
-1	64	-8

3	5	8	3
8	3	7	1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        def printMatrix(matrix):
            for row in self.matrix:
                for x in row:
                    print("{:3d}".format(x), end="")

                print()

        return f"{printMatrix(self.matrix)}\n"

    def __add__(self, other):
        return Matrix([[self.matrix[0][0] + other.matrix[0][0], self.matrix[0][1] + other.matrix[0][1],
                        self.matrix[0][2] + other.matrix[0][2]],
                       [self.matrix[1][0] + other.matrix[1][0], self.matrix[1][1] + other.matrix[1][1],
                        self.matrix[1][2] + other.matrix[1][2]]])


matrix = Matrix([[1, 2, 3], [4, 5, 6]])
matrix_2 = Matrix([[7, 8, 9], [10, 11, 12]])

print(matrix)
print(matrix_2)
print(matrix + matrix_2)
