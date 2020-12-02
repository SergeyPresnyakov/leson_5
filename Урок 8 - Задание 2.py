# ! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу
на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой."""


class Zerodivision(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        dividend = float(input("Введите делимое: "))
        divider = float(input("Введите делитель: "))
        if divider == 0:
            raise Zerodivision("Делитель не должен быть равен нулю")


    except (Zerodivision) as err:
        print(err)
        continue

    except (ValueError, NameError):
        print("Вы должны ввести число")
        continue

    else:
        print(f"При делении {dividend} на {divider} получается {(dividend / divider):.03}")
        break
