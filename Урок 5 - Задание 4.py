#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Two — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл."""

dictionary_eng = open("text_4.txt", "r", encoding="utf-8")
dictionary_rus = open("text_4_rus.txt", "w", encoding="utf-8")

content = dictionary_eng.readlines()
dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
str = content
for string in content:
    print(dic[string.split()[0]], string.split()[1], string.split()[2], file=dictionary_rus)

dictionary_eng.close()
dictionary_rus.close()
