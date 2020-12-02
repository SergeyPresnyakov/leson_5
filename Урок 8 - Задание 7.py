# ! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата."""


class Complex:

    def __init__(self, material_num, imaginary_num):
        self.material_num = material_num
        self.imaginary_num = imaginary_num

    def __mul__(self, other):
        a = self.material_num * other.material_num - (self.imaginary_num * other.imaginary_num)
        b = self.material_num * other.material_num + (other.material_num * self.imaginary_num)
        if b >= 0:
            return f"{a} + {b}j"
        else:
            return f"{a} - {abs(b)}j"

    def __add__(self, other):
        a = self.material_num + other.material_num
        b = self.imaginary_num + other.imaginary_num
        if b >= 0:
            return f"{a} + {b}j"
        else:
            return f"{a} - {abs(b)}j"


obj_1 = Complex(-7, -3)
obj_2 = Complex(-6, -3)
print(obj_1 + obj_2)
print(obj_1 * obj_2)
