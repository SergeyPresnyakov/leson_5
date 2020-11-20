#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров)"""


class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


# Создаем класс
a = Position("Сергей", "Пресняков", "директор", 80000, 10000)
b = Position("Иван", "Смирнов", "бухгалтер", 50000, 5000)

# Проверяем значения атрибутов
print(a.name, b.name)
print(a.surname, b.surname)
print(a.position, b.position)
print(a._income, b._income)

# Вызываем методы экземпляра
print()
print(f"Доход сотрудника '{a.get_full_name()}' равен {a.get_total_income()} рублей")
print()
print(f"Доход сотрудника '{b.get_full_name()}' равен {b.get_total_income()} рублей")
