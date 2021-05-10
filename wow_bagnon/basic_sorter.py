from typing import List, Tuple, TypedDict

from wow_bagnon.bag import Bag
from wow_bagnon.item import Item, ItemType


class DictItem(TypedDict):
    id: int
    bag: int
    slot: int
    type: ItemType
    stack: int
    max_stack: int


class DictBag(TypedDict):
    id: int
    type: ItemType
    size: int
    items: List[DictItem]


class BasicSorter:
    def __init__(self, bags: List[DictBag]):
        self.bags: List[Bag] = []
        for bag in bags:
            print(bag)
            current_bag = Bag(id=bag["id"], item_type=bag["type"], size=bag["size"])
            for item in bag["items"]:
                current_bag.put(
                    item=Item(
                        id=item["id"],
                        max_stack=item["max_stack"],
                        stack=item["stack"],
                        type=item["type"],
                    ),
                    slot=item["slot"],
                )
            self.bags.append(current_bag)

    def sort(self) -> Tuple[List[DictBag], List[DictItem]]:
        return [], []


if __name__ == "__main__":
    bags = [
        {
            "id": 1,
            "size": 20,
            "type": 0,
            "items": [
                {"bag": 1, "slot": 1, "id": 2, "stack": 3, "max_stack": 10, "type": 8},
                {"bag": 1, "slot": 2, "id": 3, "stack": 15, "max_stack": 20, "type": 2},
                {"bag": 1, "slot": 3, "id": 2, "stack": 8, "max_stack": 10, "type": 8},
                {"bag": 1, "slot": 5, "id": 1, "stack": 1, "max_stack": 1, "type": 0},
                {"bag": 1, "slot": 9, "id": 1, "stack": 1, "max_stack": 1, "type": 0},
            ],
        },
        {"id": 2, "size": 6, "type": 8, "items": []},
        {"id": 3, "size": 6, "type": 2, "items": []},
    ]
    BasicSorter(bags=bags)  # type: ignore
