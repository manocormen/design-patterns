"""Open-Closed Principle (OCP)

A class is open for extension but closed for modification.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Iterator, List

Color = Enum("Color", ["RED", "GREEN", "BLUE"])
Size = Enum("Size", ["SMALL", "MEDIUM", "LARGE"])


class Product:
    """Model product."""

    def __init__(self, name: str, color: Color, size: Size):
        """Initialize product."""
        self.name = name
        self.color = color
        self.size = size


class Specification(ABC):
    """Model specification."""

    @abstractmethod
    def is_satisfied(self, item: Product):
        """Check if item satisfies specification."""

    def __and__(self, other):
        """Combine two specifications."""
        return AndSpecification(self, other)


class AndSpecification(Specification):
    """Combine two specifications."""

    def __init__(self, *specs: Specification):
        """Initialize combined specification."""
        self.specs = specs

    def is_satisfied(self, item: Product) -> bool:
        """Check if item satisfies all specifications."""
        return all(spec.is_satisfied(item) for spec in self.specs)


class ColorSpecification(Specification):
    """Model color specification."""

    def __init__(self, color: Color):
        """Initialize color specification."""
        self.color = color

    def is_satisfied(self, item: Product) -> bool:
        """Check if item satisfies color specification."""
        return item.color == self.color


class SizeSpecification(Specification):
    """Model size specification."""

    def __init__(self, size: Size):
        """Initialize color specification."""
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        """Check if item satisfies size specification."""
        return item.size == self.size


class Filter(ABC):
    """Model filter."""

    @staticmethod
    @abstractmethod
    def filter(items: List[Product], spec: Specification):
        """Filter products according to specification."""


class ProductFilter(Filter):
    """Model filter."""

    @staticmethod
    def filter(items: List[Product], spec: Specification) -> Iterator[Product]:
        """Filter products according to specification."""
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    green = ColorSpecification(Color.GREEN)
    print("Green products:")
    for product in ProductFilter.filter(products, green):
        print(f" - {product.name} is green")

    large = SizeSpecification(Size.LARGE)
    print("Large products:")
    for product in ProductFilter.filter(products, large):
        print(f" - {product.name} is large")

    blue = ColorSpecification(Color.BLUE)
    blue_large = blue & large
    print("Blue and large products:")
    for product in ProductFilter.filter(products, blue_large):
        print(f" - {product.name} is blue and large")
