# ! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

# class Clothes6:
#     def __init__(self, param):
#         self.param = param

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consump(self):
        pass


class Coat(Clothes):

    def __init__(self):
        self.size_coat = int(input("Введите размер пальто: "))

    @property
    def fabric_consump(self):
        return self.size_coat / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self):
        self.size_suit = int(input("Введите рост костюма: "))

    @property
    def fabric_consump(self):
        return self.size_suit * 0.02 + 0.3


mc_1 = Coat()
mc_2 = Suit()
print(f"Общий рахсод ткани составляет {(float(mc_1.fabric_consump) + float(mc_2.fabric_consump)):.4} кв. м.")
