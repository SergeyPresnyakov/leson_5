#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран."""
numbers = open("numbers.txt", "r+", encoding="utf-8")
numbers.write(input("Введите строку чисел, разделенных пробелами: "))
numbers = open("numbers.txt", "r", encoding="utf-8")
content = numbers.read()
print(f"Сумма, введенных Вами чисел = {sum([int(item) for item in content.split()])}")
numbers.close()
