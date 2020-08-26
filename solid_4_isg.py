"""Interfact Segregation Principle

Favor many client-specific interfaces over a single general-purpose one.
"""

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass


class Photocopier(Printer, Scanner):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def photocopy(self):
        pass


class ActualPrinter(Printer):
    def print(self):
        print("printed document")


class ActualFax(Photocopier, Fax):
    def print(self):
        print("printed document")

    def scan(self):
        print("scanned document")

    def fax(self):
        print("faxed document")

    def photocopy(self):
        self.scan()
        self.print()


if __name__ == "__main__":
    print("Use my printer:")
    my_printer = ActualPrinter()
    my_printer.print()

    print("Use my fax:")
    my_fax = ActualFax()
    my_fax.print()
    my_fax.scan()
    my_fax.fax()
    my_fax.photocopy()
