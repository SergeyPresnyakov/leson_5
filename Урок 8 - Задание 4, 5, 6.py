# ! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП."""

receipt_stock_printer = 0
receipt_stock_scanner = 0
receipt_stock_copier = 0
receipt_marketing_printer = 0
receipt_marketing_scanner = 0
receipt_marketing_copier = 0
receipt_production_printer = 0
receipt_production_scanner = 0
receipt_production_copier = 0

global base_2

dic = {"1": "Принтер", "2": "Сканер", "3": "Ксерокс"}


class Stock:
    global printer_stock
    global scanner_stock
    global copier_stock
    global printer_marketing
    global scanner_marketing
    global copier_marketing
    global printer_production
    global scanner_production
    global copier_production
    global base_2
    print()
    print("Для начала работы с базой данных склада оргтехники необходмо провести инвентаризацию")
    print()

    while True:
        try:
            print()
            printer_stock = int(input("Введите количество принтеров на складе: "))
            scanner_stock = int(input("Введите количество сканеров на складе: "))
            copier_stock = int(input("Введите количество ксероксов на складе: "))
            printer_marketing = int(input("Введите количество принтеров в отделе маркетинг: "))
            scanner_marketing = int(input("Введите количество сканеров в отделе маркетинг: "))
            copier_marketing = int(input("Введите количество ксероксов в отделе маркетинг: "))
            printer_production = int(input("Введите количество принтеров на производстве: "))
            scanner_production = int(input("Введите количество сканеров на производстве: "))
            copier_production = int(input("Введите количество ксероксов на производстве: "))
            break
        except:
            print()
            print("Вы ввели не число, введите целое число")
            continue

    def base(self, receipt_stock_printer, receipt_stock_scanner, receipt_stock_copier, receipt_marketing_printer,
             receipt_marketing_scanner, receipt_marketing_copier, receipt_production_printer,
             receipt_production_scanner, receipt_production_copier):

        return [
            {"Принтер": printer_stock + receipt_stock_printer, "Сканер": scanner_stock + receipt_stock_scanner,
             "Ксерокс": copier_stock + receipt_stock_copier},
            {"Принтер": printer_marketing + receipt_marketing_printer,
             "Сканер": scanner_marketing + receipt_marketing_scanner,
             "Ксерокс": copier_marketing + receipt_marketing_copier},
            {"Принтер": printer_production + receipt_production_printer,
             "Сканер": scanner_production + receipt_production_scanner,
             "Ксерокс": copier_production + receipt_production_copier}
        ]

    def movement(self):

        while True:
            print()
            print("Меню:")
            print("--------------------------------------------------")
            print("Выберете действие и введите соответсвующую цифру:")
            print("'1' - Принять товар на склад")
            print("'2' - Передать оргтехнику со склада в подразделения")
            print("'3' - Вывести статистику по количеству оргтехники")
            print("'4' - Закончить работу с базой")
            print()
            action = input("Введите цифру: ")

            global receipt_stock_printer
            global receipt_stock_scanner
            global receipt_stock_copier
            if action == '1':
                while True:
                    try:
                        print()
                        receipt_stock_printer = int(input("Введите количество принтеров поступивших на склад: "))
                        receipt_stock_scanner = int(input("Введите количество сканеров поступивших на склад: "))
                        receipt_stock_copier = int(input("Введите количество ксероксов поступивших на склад: "))
                        base_2 = Stock().base(receipt_stock_printer, receipt_stock_scanner, receipt_stock_copier,
                                              receipt_marketing_printer, receipt_marketing_scanner,
                                              receipt_marketing_copier, receipt_production_printer,
                                              receipt_production_scanner,
                                              receipt_production_copier)
                        break
                    except:
                        print()
                        print("Вы ввели не число, введите целое число")
                        continue

                print(base_2)
                continue

            if action == '2':
                while True:
                    while True:
                        print()
                        num_office_equipment = input("Принтер - 1\n"
                                                     "Сканер - 2\n"
                                                     "Ксерокс - 3\n"
                                                     "Введите номер техники, которую вы хотите передать со склада в подразделение: ")
                        if num_office_equipment == '1' or num_office_equipment == '2' or num_office_equipment == '3':

                            break
                        else:
                            print("Вы ввели не верные данные, введите цифры '1', '2', '3'")
                            continue
                    try:
                        print()
                        count_equipment = int(input("Введите количество техники, которое вы хотите передать "
                                                    "со склада в подразделение: "))

                        break
                    except:
                        print()
                        print("Вы ввели не число, введите целое число")
                        continue

                while True:
                    try:
                        print()
                        num_department = int(input("Маркетинг - 1\n"
                                                   "Производство - 2\n"
                                                   "Введите номер подразделения, в которое Вы хотите передать технику со склада: "))

                        break
                    except:
                        print()
                        print("Вы ввели не число, введите целое число")
                        continue

                base_2 = Stock().base(receipt_stock_printer, receipt_stock_scanner, receipt_stock_copier,
                                      receipt_marketing_printer, receipt_marketing_scanner,
                                      receipt_marketing_copier, receipt_production_printer,
                                      receipt_production_scanner, receipt_production_copier)

                if base_2[0][dic[num_office_equipment]] - count_equipment < 0:
                    print()
                    print(
                        f"Вы хотите передать {count_equipment} единиц техники, а ее на складе числится {base_2[0][dic[num_office_equipment]]}")
                    continue

                base_2[num_department][num_office_equipment] = base_2[num_department][
                                                                   dic[num_office_equipment]] + count_equipment
                base_2[0][num_office_equipment] = base_2[0][dic[num_office_equipment]] - count_equipment

                print("Cтатус движения запасов", base_2[0])

            base_2 = Stock().base(receipt_stock_printer, receipt_stock_scanner, receipt_stock_copier,
                                  receipt_marketing_printer, receipt_marketing_scanner,
                                  receipt_marketing_copier, receipt_production_printer,
                                  receipt_production_scanner, receipt_production_copier)

            if action == '3':

                while True:
                    while True:
                        print()
                        num_report = input("Аналитика по складу - 1\n"
                                           "Аналитика по отделу маркетинга - 2\n"
                                           "Аналитика по производству - 3\n"
                                           "Введите вариант отчета: ")
                        if num_report == '1' or num_report == '2' or num_report == '3':

                            break
                        else:
                            print("Вы ввели не верные данные, введите цифры '1', '2', '3'")
                            continue

                    if num_report == '1':
                        Stock_2().show_info()
                        Stock_2().count(base_2, 0)

                    if num_report == '2':
                        Marketing().show_info()
                        Marketing().count(base_2, 1)

                    if num_report == '3':
                        Production().show_info()
                        Production().count(base_2, 2)

                    break
                continue

            if action == '4':
                print("Работа с базой закончена")
                break

            if action != '1' or action != '2' or action != '3' or action != '4':
                print("Вы ввели неверную команду, введите '1', '2', '3' или '4'")
                continue


class Department:
    def __init__(self):
        pass

    def count(self, basa, type_department):
        for key, value in basa[type_department].items():
            print(f"{key} - {value} шт.")


class Stock_2(Department):

    def show_info(self):
        print()
        print("Структура запасов отдела склад:")


#
class Marketing(Department):

    def show_info(self):
        print()
        print("Структура запасов отдела маркетинга")


class Production(Department):

    def show_info(self):
        print()
        print("Структура запасов отдела производства")


Stock().movement()
