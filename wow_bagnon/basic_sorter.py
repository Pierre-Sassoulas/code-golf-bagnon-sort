from typing import List, TypedDict

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


class DictMove(TypedDict):
    bag_origin: int
    slot_origin: int
    bag_destination: int
    slot_destination: int


class BasicSorter:
    def __init__(self, bags: List[DictBag]):
        self.bags: List[Bag] = []
        for bag in bags:
            current_bag = Bag(id=bag["id"], item_type=bag["type"], size=bag["size"])
            for item in bag["items"]:
                current_item = Item(
                    id=item["id"],
                    max_stack=item["max_stack"],
                    stack=item["stack"],
                    type=item["type"],
                )
                current_bag.put(item=current_item, slot=item["slot"])
            self.bags.append(current_bag)

    def apply_move(self, ticks: List[List[DictMove]]):
        for moves in ticks:
            for move in moves:
                item = self.bags[move["bag_origin"]].pick(move["slot_origin"])
                self.bags[move["bag_destination"]].put(
                    item, slot=move["slot_destination"]
                )
        print(f"Final result: {self.bags}")
