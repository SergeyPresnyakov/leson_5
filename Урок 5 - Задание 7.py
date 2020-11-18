# ! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста."""

import json

with open("text_7.txt", "r", encoding="utf-8") as organizations:
    profit_org = {}
    los_org = {}
    for string in organizations.readlines():
        profit_org.update({string.split()[0]: int(string.split()[2]) - int(string.split()[3])})

average_profit = {"average_profit": int(sum([el for el in profit_org.values() if el >= 0])
                                        / len([el for el in profit_org.values() if el >= 0]))}

for el in [el for el in profit_org.keys() if profit_org[el] < 0]:
    los_org.update({el: profit_org[el]})

list_companies = [profit_org, average_profit, los_org]
print(list_companies)

with open("text_77_my.json", "w") as text_77_my:
    json.dump(list_companies, text_77_my)
