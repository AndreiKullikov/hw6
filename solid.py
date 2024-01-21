#1) Переписать код в соответствии с Single Responsibility Principle:

from datetime import date

class Employee:
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name}, dob - {self.dob}"

class SalaryCalculator:
    @staticmethod
    def calculate_net_salary(base_salary):
        tax = int(base_salary * 0.25)  # рассчитать налог другим способом
        return base_salary - tax
# 2) Переписать код SpeedCalculation в соответствии с Open-Closed Principle:
class Vehicle:
    def __init__(self, max_speed, vehicle_type):
        self.max_speed = max_speed
        self.type = vehicle_type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type

class Car(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.8

class Bus(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.6

class SpeedCalculation:
    def calculate_allowed_speed(self, vehicle):
        return vehicle.calculate_allowed_speed()

#3) Переписать код в соответствии с Interface Segregation Principle:
from abc import ABC, abstractmethod
import math

class AreaCalculatable(ABC):
    @abstractmethod
    def area(self):
        pass

class VolumeCalculatable(ABC):
    @abstractmethod
    def volume(self):
        pass

class Circle(AreaCalculatable):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius

class Cube(AreaCalculatable, VolumeCalculatable):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge
