https://codegolf.meta.stackexchange.com/questions/2140/sandbox-for-proposed-challenges?answertab=active#tab-top

# WOW, sort this bag, this is a paralleled mess!

Bagnon is an add-on by Jaliborc for World of Warcraft (WOW), which has a sorting feature
included. The goal of this challenge is to make this sorting faster. The winner gets to
be ported to Lua and gets to be proposed as a merge request in
[WildPants the sorting library that Bagnon and Combductor rely on](https://github.com/tullamods/Wildpants/blob/29fbaf502b2780010b735f1af8af0ba5702afbbf/api/sorting.lua#L21).
This would affect a lot of WOW players. Please don't flood Jaliborc with an inferior
algorithm, the man is busy.

- In WOW, there are up to 5 bags with each a number of slots. From 20 slots (just the
  starting bag) to 164 slots (20 + 4 _ 36 slot bags). There is also a 98 slots bag (the
  reagent bank), and the bank itself which has between 28 (starting bank space) and a
  maximum of 280 slots (28 + 7 _ 36 slots bags).
- Bags and items have types: There are special bags that can only contain one type of
  object. For example, quivers can only contain arrows, but arrows can be stored
  everywhere.
- Items have a stack size: A stack of 200 arrows take a slot, but a sword takes a single
  slot.
- Item cannot be together in the same slot: One arrow alone takes the full slot.

Bagnon hides this from the user by creating a single bag that you can sort. Bank bags
and reagent bags are sorted less often and independently to the player bags.

In order to sort the bag, you need to move the item. A move is done by calling the WOW
API:

- Moving something can fail if the slot does not accept this type of object.
- Moving something to a slot where another item exists invert item position and it can
  fail if one of the slots does not accept these types of items.
- Moving an item that can be stacked from a slot A to slot B where the same object
  exists, makes the stack in slot B bigger, and every item that overflow goes into slot
  A (slot A can become empty as a result).

Moving an item requires a server call and is one of the two limiting factors. Let's call
this `serverDelayTime`. If you try to move an item again faster than the
`serverDelayTime` it will fail.

But the sorting can be parallelized: every `serverDelayTime` you can exchange the
position of multiple items as long as no action occurred on any of them. Although some
clients freeze when you move too many objects this way at the same time. This can vary
between clients with their PC performances. Let's call this second limiting factor
`maxConcurrentMove` (Value is from 1 for two objects moved at a time to 140 for every
object in the biggest bank moved at the same time).

Input: List of items and bags

```python
items = [
    {"id": 1, "bag": 1, "slot": 4, "stack": 20, "type": 0},
    {"id": 5, "bag": 1, "slot": 5, "stack": 200, "itemCount": 187, "type": 3},
    {"id": 5, "bag": 1, "slot": 5, "stack": 200, "itemCount": 25, "type": 3},
]
bags = [
    {"bag": 0, "types": [0, 1, 2, 3], "size": 20},
    {"bag": 1, "types": [0, 1, 2, 3], "size": 16},
    {"bag": 2, "types": [0, 1, 2, 3], "size": 14},
    {"bag": 2, "types": [3], "size": 14},
]
```

Output: List of tick calls. Each tick is a list of move calls.

Applying all the moves must return sorted bags. Ie: item's id are from smallest to
biggest.

This is a real-world algorithm, so of course, the theoretically faster algorithm wins !
The objective is to sort the bag in the less possible tick of `serverDelayTime` while
respecting the `maxConcurrentMove` limit and without moving anything to a forbidden bag.
For the same number of ticks, the winner is the one with the least move call.
