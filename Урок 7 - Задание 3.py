# ! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого)
деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных
 двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке."""


class Cell():
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return (f"Сумма аргументов классов равна {self.cell + other.cell}")

    def __sub__(self, other):
        return (
            f"Разность аргументов классов равна {self.cell - other.cell}") if self.cell - other.cell > 0 else "Разность аргументов классов меньше либо равна нулю"

    def __mul__(self, other):
        return (f"Произведение аргументов классов равно {self.cell * other.cell}")

    def __floordiv__(self, other):
        return (f"Результат целочисленного деления аргументов классов равно {self.cell // other.cell}")

    def make_order(self, row):
        self.row = row
        for i in range(self.cell // row):
            for j in range(row):
                print("*", end="")
            print()
        for k in range(self.cell % row):
            print("*", end="")


с_1 = Cell(17)
с_2 = Cell(18)

print(с_1 + с_2)
print(с_1 - с_2)
print(с_1 * с_2)
print(с_1 // с_2)
print()
с_2.make_order(4)
