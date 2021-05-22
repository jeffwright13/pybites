"""
Original tests (which fail):

from inventory import items, duplicate_items

def test_change_copy_only():
    items_copy = duplicate_items(items)
    assert items == items_copy

    # modify the copy
    items_copy[0]['name'] = 'macbook'
    items_copy[1]['id'] = 4
    items_copy[2]['value'] = 30

    # only copy should have been updated, check original items values
    assert items[0]['name'] == 'laptop'
    assert items[1]['id'] == 2
    assert items[2]['value'] == 20
"""
from bite032 import duplicate_items, copy_items, deepcopy_items


def test_duplicate():
    items = [
        {"id": 1, "name": "laptop", "value": 1000},
        {"id": 2, "name": "chair", "value": 300},
        {"id": 3, "name": "book", "value": 20},
    ]
    items_copy = duplicate_items(items)
    assert items == items_copy

    # modify the copy
    items_copy[0]["name"] = "macbook"
    items_copy[1]["id"] = 4
    items_copy[2]["value"] = 30

    # both copy & original have been updated
    assert items[0]["name"] == "macbook"
    assert items[1]["id"] == 4
    assert items[2]["value"] == 30


def test_copy():
    items = [
        {"id": 1, "name": "laptop", "value": 1000},
        {"id": 2, "name": "chair", "value": 300},
        {"id": 3, "name": "book", "value": 20},
    ]

    items_copy = copy_items(items)
    assert items == items_copy

    # modify the copy
    items_copy[0]["name"] = "macbook"
    items_copy[1]["id"] = 4
    items_copy[2]["value"] = 30

    # both copy & original have been updated
    assert items[0]["name"] == "macbook"
    assert items[1]["id"] == 4
    assert items[2]["value"] == 30


def test_deep_copy():
    items = [
        {"id": 1, "name": "laptop", "value": 1000},
        {"id": 2, "name": "chair", "value": 300},
        {"id": 3, "name": "book", "value": 20},
    ]

    items_copy = deepcopy_items(items)
    assert items == items_copy

    # modify the copy
    items_copy[0]["name"] = "macbook"
    items_copy[1]["id"] = 4
    items_copy[2]["value"] = 30

    # only copy should have been updated, check original items values
    assert items[0]["name"] == "laptop"
    assert items[1]["id"] == 2
    assert items[2]["value"] == 20
