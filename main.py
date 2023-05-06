import dataclasses


@dataclasses.dataclass
class Item:
    weight: int
    width: int
    height: int


i = Item(10, 52, 31)
i1 = Item(10, 52, 31)
print(i == i1)


class Item:
    def __init__(self, weight, width, height):
        self.weight = weight
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.weight == other.weight

    def __str__(self):
        pass


class Electronics(Item):
    def __init__(self, power_usage, power):
        pass


i = Item(10, 56, 31)
i1 = Item(10, 52, 31)
print(i == i1)