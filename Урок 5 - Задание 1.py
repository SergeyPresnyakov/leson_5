"""Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""

text_1 = open("text_1.txt", "w", encoding="utf-8")

while True:
    str_list = input("Введите строку: ")
    if str_list == "":
        break
    text_1.write(str_list)
    text_1.write('\n')
text_1.close()
