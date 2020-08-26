"""Dependency Inversion Principle (DIP)

Classes should depend on abstractions, not on lower-level concretions.
"""

from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Steak(Food):  # Low-level class
    def cook(self):
        print("Cook steak")

    def eat(self):
        print("Eat steak")


class Rice(Food):  # Low-level class
    def cook(self):
        print("Cook rice")

    def eat(self):
        print("Eat rice")


class Dinner:  # High-level class
    def __init__(self, food: Food):  # Depend on abstraction (Food)
        self.food = food

    def prepare(self):
        self.food.cook()

    def consume(self):
        self.food.eat()


if __name__ == "__main__":
    wagyu = Steak()
    romantic_dinner = Dinner(wagyu)
    romantic_dinner.prepare()
    romantic_dinner.consume()
