class NPC:

    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __str__(self):
        return f"{self.name}, {self.size}, {self.type}"

    def __repr__(self):
        return f"{self.name}, {self.size}, {self.type}"
