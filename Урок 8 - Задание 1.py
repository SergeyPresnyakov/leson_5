# ! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных."""


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def num(cls, data):
        day, month, year = data
        return cls(day, month, year)

    @staticmethod
    def valid_num():
        if date_split.day > 31 or date_split.day < 1:
            print("Вы указали недопустимое значение дня. Введите день в интервале от 1 до 31")
            print()
            return input_data()

        elif date_split.month > 12 or date_split.month < 1:
            print("Вы указали недопустимое значение месяца. Введите месяц в интервале от 1 до 12")
            print()
            return input_data()

        elif date_split.year > 9999 or date_split.year < 0:
            print("Вы указали недопустимое значение года. Введите год в интервале от 0 до 9999")
            print()
            return input_data()


def input_data():
    global data, date_split
    while True:
        try:
            data = [int(el) for el in
                    input("Введите дату в формате 'день-месяц-год' (целыми числами): ").replace('-', ' ').split()]
            date_split = Date.num(data)
            Date.valid_num()
            print()
            print("Вы ввели корректные данные")
            print()
            print(f"Номер дня месяца {(date_split.day):02}")
            print(f"Номер месяца {(date_split.month):02}")
            print(f"Год {(date_split.year):04}")
            break

        except:
            print("Вы ввели неправильны формат даты")
            print()
            return input_data()


input_data()
