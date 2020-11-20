#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра."""


class Stationery():
    def __init__(self, title):
        self.title = title

    def drow(self):
        print(f"Запуск отрисовки с помощью иннструмента '{self.title}'")


class Pen(Stationery):

    def drow(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def drow(self):
        print("Запуск отрисовки карандашем")


class Handle(Stationery):
    def drow(self):
        print("Запуск отрисовки маркером")


a = Stationery("Неизветная пренадлежность")
a.drow()

b = Pen("Pen")
b.drow()

с = Pencil("Pencil")
с.drow()

d = Handle("Handle")
d.drow()
