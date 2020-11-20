#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police == False:
            print(
                f"Автомобиль {self.color} {self.name}, который не является полицейским поехал со скоростью {self.speed} км/ч")
        else:
            print(f"Полицейский автомобиль {self.color} {self.name} поехал со скоростью {self.speed} км/ч")

    def show_speed(self):
        print(f"Автомобиль {self.color} {self.name} двигается со скоростью {self.speed} км/ч")

    def turn(self, direction):
        print(f"Автомобиль {self.color} {self.name} повернул {direction}")

    def stop(self):
        print(f"Автомобиль {self.color} {self.name} остановился")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Зафиксировано превышение скорости")
        else:
            print(f"Автомобиль {self.color} {self.name} двигается с допустимой скоростью")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Зафиксировано превышение скорости")
        else:
            print(f"Автомобиль {self.color} {self.name} двигается с допустимой скоростью")


class PoliceCar(Car):
    pass


# TownCar

towncar = TownCar(70, "red", "Lada", False)
towncar.go()
towncar.show_speed()
towncar.turn("направо")
towncar.speed = 50
towncar.show_speed()
towncar.turn("налево")
towncar.stop()
print()

# SportCar(Car)
sportcar = SportCar(50, "green", "Ferrari", False)
sportcar.go()
sportcar.show_speed()
sportcar.turn("направо")
sportcar.speed = 150
sportcar.show_speed()
sportcar.turn("налево")
sportcar.stop()
print()

# WorkCar(Car)
workcar = WorkCar(50, "black", "Volvo", False)
workcar.go()
workcar.show_speed()
workcar.turn("направо")
workcar.speed = 30
workcar.show_speed()
workcar.turn("налево")
workcar.stop()
print()

# PoliceCar(Car)
policecar = PoliceCar(100, "white", "Forf", True)
policecar.go()
policecar.show_speed()
policecar.turn("направо")
policecar.speed = 30
policecar.show_speed()
policecar.turn("налево")
policecar.stop()
