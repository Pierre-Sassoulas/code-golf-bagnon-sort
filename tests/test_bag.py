def test_bags(bags):
    msgs = [
        "Bag 1 (ItemType.STANDARD - 20)",
        '1: "bag": 1, "slot": 1, "id": 2, "stack": 3, "max_stack": 10, "type": SOUL',
        '2: "bag": 1, "slot": 2, "id": 3, "stack": 15, "max_stack": 20, "type": ENCHANTING',
        '3: "bag": 1, "slot": 3, "id": 2, "stack": 8, "max_stack": 10, "type": SOUL',
        '5: "bag": 1, "slot": 5, "id": 1, "stack": 1, "max_stack": 1, "type": STANDARD',
        '9: "bag": 1, "slot": 9, "id": 1, "stack": 1, "max_stack": 1, "type": STANDARD',
    ]
    assert all([x in str(bags[0]) for x in msgs])
