from wow_bagnon.basic_sorter import BasicSorter


def test_bags():
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
    sorter = BasicSorter(bags=bags)  # type: ignore
    ticks = [
        [],
        [],
    ]
    sorter.apply_move(ticks)
