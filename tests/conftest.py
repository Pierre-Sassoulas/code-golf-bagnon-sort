import pytest

from wow_bagnon.bag import Bag
from wow_bagnon.item import Item, ItemType


@pytest.fixture
def standard_bag():
    return Bag(id="1", size=20, item_type=ItemType.STANDARD)


@pytest.fixture
def soul_bag():
    return Bag(id="2", size=6, item_type=ItemType.SOUL)


@pytest.fixture
def enchanting_bag():
    return Bag(id="3", size=6, item_type=ItemType.ENCHANTING)


@pytest.fixture
def bags(standard_bag, soul_bag, enchanting_bag):
    weapon = Item(id=1, max_stack=1, stack=1, type=ItemType.STANDARD)
    same_weapon = Item(id=1, max_stack=1, stack=1, type=ItemType.STANDARD)
    stacked_soul = Item(id=2, max_stack=10, stack=3, type=ItemType.SOUL)
    other_stacked_soul = Item(id=2, max_stack=10, stack=8, type=ItemType.SOUL)
    dust = Item(id=3, max_stack=20, stack=15, type=ItemType.ENCHANTING)
    standard_bag.put(slot=5, item=weapon)
    standard_bag.put(slot=9, item=same_weapon)
    standard_bag.put(slot=1, item=stacked_soul)
    standard_bag.put(slot=3, item=other_stacked_soul)
    standard_bag.put(slot=2, item=dust)
    return [standard_bag, soul_bag, enchanting_bag]
