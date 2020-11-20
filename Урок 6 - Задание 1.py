#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
 (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
  красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
  второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.  Переключение между режимами
  должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
  создав экземпляр и вызвав описанный метод.
  Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
  соответствующее сообщение и завершать скрипт."""

# Настраиваемый по времени светофор
# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from random import *
from tkinter import *


# Настраиваемый по времени светофор
class TrafficLight:

    def running(self, time_red, time_yellow, time_green):
        size = 300
        root = Tk()
        canvas = Canvas(root, width=size, height=size)
        while True:
            canvas.pack()
            canvas.create_oval(0, 200, 100, 100, fill="white")
            canvas.create_oval(0, 300, 100, 200, fill="white")
            canvas.create_oval(0, 100, 100, 0, fill="red")
            root.update()
            time.sleep(time_red)

            # print("\033[31m {}".format("Горит красный"))
            canvas.pack()
            canvas.create_oval(0, 200, 100, 100, fill="yellow")
            canvas.create_oval(0, 100, 100, 0, fill="white")
            root.update()
            time.sleep(time_yellow)

            # print("\033[33m {}".format("Горит желтый"))
            canvas.pack()
            canvas.create_oval(0, 300, 100, 200, fill="green")
            canvas.create_oval(0, 200, 100, 100, fill="white")
            root.update()
            time.sleep(time_green)

            # print("\033[32m {}".format("Горит зеленый"))
            canvas.pack()
            canvas.create_oval(0, 200, 100, 100, fill="yellow")
            canvas.create_oval(0, 300, 100, 200, fill="white")
            root.update()
            time.sleep(time_yellow)
            # print("\033[33m {}".format("Горит желтый"))


t = TrafficLight()
t.running(5, 2, 5)
