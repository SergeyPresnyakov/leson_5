# ! /usr/bin/env python
# -*- coding: utf-8 -*-

lessons = open("text_6.txt", "r", encoding="utf-8")
dic = {}
for string in lessons.readlines():
    number_all = ''
    for word in string.split():
        number = ""
        for letter in str(word):
            if "0" <= letter <= "9":
                number = number + letter
                continue
            else:
                break
        number_all = number + ' ' + number_all
    dic.update({string.split()[0]: sum([int(item) for item in number_all.split()])})
print(dic)
