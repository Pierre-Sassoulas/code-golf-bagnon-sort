from typing import List, Optional

from wow_bagnon.item import Item, ItemType


class Bag:
    def __init__(self, id: int, size: int, item_type: ItemType = ItemType.STANDARD):
        self.id: int = id
        self.size: int = size
        self.slots: List[Optional[Item]] = [None] * size
        self.item_type: ItemType = item_type

    def __str__(self):
        repr = f"Bag {self.id} ({self.item_type} - {self.size})\n"
        for i, slot in enumerate(self.slots):
            if slot is not None:
                repr += f"\t{i}: {slot.__repr__().format(bag=self.id, slot=i)}\n"
        return repr

    def __repr__(self):
        repr = (
            f'{{"id": {self.id}, "size": {self.size}, "type": {self.item_type.value}, '
        )
        items = []
        for i, slot in enumerate(self.slots):
            if slot is not None:
                items.append("{%s}" % slot.__repr__().format(bag=self.id, slot=i))
        return repr + '"items": [' + ", ".join(items) + "]}"

    def pick(self, slot: int) -> Optional[Item]:
        try:
            item = self.slots[slot]
        except KeyError:
            raise RuntimeError(
                f"Tried to pick an item from slot {slot} that does not exist in {self}"
            )
        self.slots[slot] = None
        return item

    def stack(self, slot, item: Item) -> Optional[Item]:
        other = self.slots[slot]
        assert_msg = f"Trying to stack {other} and {item}, that ain't gonna work"
        assert other.id == item.id, assert_msg
        assert other.max_stack == item.max_stack, assert_msg
        assert other.type == item.type, assert_msg
        total_item = other.stack + item.stack
        other.stack = max(other.max_stack, total_item)
        return Item(
            id=other.id,
            stack=other.stack - total_item,
            max_stack=other.max_stack,
            type=other.type,
        )

    def put(self, item: Optional[Item], slot: int) -> Optional[Item]:
        existing_item = self.pick(slot)
        if item is None:
            return existing_item
        if self.item_type != ItemType.STANDARD and item.type != self.item_type:
            raise RuntimeError(
                f"Tried to put an item with type {item.type} in bag that can handle type {self.item_type}"
            )
        try:
            self.slots[slot] = item
        except KeyError:
            raise RuntimeError(
                f"Tried to put an item in slot {slot} that does not exist in {self}"
            )
        if existing_item is None:
            return None
        if item.id != existing_item.id or item.max_stack == 1:
            return existing_item
        return self.stack(slot, existing_item)
