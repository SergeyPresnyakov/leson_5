#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""

my_f = open("text_1.txt", "r", encoding="utf-8")
content = my_f.readlines()
print("Количество строк в документе = ", len(content))
for string in content:
    string = string.replace('\n', '')
    print(f"Количество слов в строке '{string}' = {len(string.split())}")
my_f.close()
