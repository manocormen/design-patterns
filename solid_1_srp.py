"""Single-Responsibility Principle (SRP)

A class should have only one responsibility.
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, index):
        del self.entries[index]

    def __str__(self):
        return "\n".join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as file:
            file.write(str(journal))

    @staticmethod
    def load_from_file(filename):
        with open(filename) as file:
            return file.read()


if __name__ == "__main__":
    journal = Journal()
    journal.add_entry("I cried today.")
    journal.add_entry("I ate a bug.")

    print(f"Journal entries:\n{journal}")

    PersistenceManager.save_to_file(journal, "./tmp/journal.txt")
    journal_txt = PersistenceManager.load_from_file("./tmp/journal.txt")
    print(f"Journal loaded entries:\n{journal_txt}")
