import enum
from typing import Union


class ItemType(enum.Enum):
    STANDARD = 0
    QUIVER = 1
    ENCHANTING = 2
    ENGINEERING = 3
    GEM = 4
    HERB = 5
    LEATHER_WORKING = 6
    MINING = 7
    SOUL = 8
    AMMO_POUCH = 9


class Item:
    # pylint: disable=redefined-builtin
    def __init__(self, id: int, stack: int, max_stack: int, type: Union[ItemType, int]):
        self.id = id
        self.stack = stack
        self.max_stack = max_stack
        if isinstance(type, int):
            type = ItemType(type)
        self.type = type

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.stack == other.stack
            and self.max_stack == other.max_stack
            and self.type == other.type
        )

    def __repr__(self):
        return '"bag": {{bag}}, "slot": {{slot}}, "id": {}, "stack": {}, "max_stack": {}, "type": {}'.format(
            self.id, self.stack, self.max_stack, self.type.name
        )

    def __gt__(self, other):
        return self.id.__gt__(other.id)