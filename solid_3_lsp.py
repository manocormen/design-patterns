"""Liskov Substitution Principle (LSP)

If you replace a class with a subclass, it shouldn't throw an error.
"""


class HistoricalEvent:
    """Model historical event."""

    def __init__(self, event_name, year):
        """Initialize historical event."""
        self.event_name = event_name
        self.year = year

    def __eq__(self, other):
        """Define equality."""
        return self.year == other.year

    def __lt__(self, other):
        """Define less than."""
        return self.year < other.year


class EventInHistory(HistoricalEvent):
    """Model historical event that took place in History."""

    def __init__(self, event_name, year):
        """Initialize historical event."""
        super().__init__(event_name, year)
        self.writing_invented = True


class EventInPrehistory(HistoricalEvent):
    """Model historical event that took place in Prehistory."""

    def __init__(self, event_name, year):
        """Initialize historical event."""
        super().__init__(event_name, year)
        self.writing_invented = False


class EventBeforeBigBang(HistoricalEvent):
    """Model historical event that took place before the Big Bang."""

    def __init__(self, event_name, year):
        """Initialize historical event."""
        super().__init__(event_name, None)  # Since time didn't "exist"
        self.writing_invented = False


def which_came_first(event1, event2):
    """Return event that came first."""
    if event1 < event2:
        first = event1.event_name
    else:
        first = event2.event_name
    return f"{first} came first."


if __name__ == "__main__":
    nine_eleven = HistoricalEvent("9/11", 2001)
    america_discovery = EventInHistory("America's discovery", 1492)
    wheel_invention = EventInPrehistory("The invention of the wheel", -3500)
    initial_singularity = EventBeforeBigBang("The creation of the universe", "N/A")

    print(which_came_first(nine_eleven, america_discovery))
    print(which_came_first(wheel_invention, america_discovery))
    print(which_came_first(nine_eleven, initial_singularity))  # Error
    # The last line breaks LSP since the same function worked with a
    # base class instance but failed with a derived class one.
