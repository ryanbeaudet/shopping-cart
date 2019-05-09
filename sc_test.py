from shopping_cart import *
import pytest

def test_to_usd():
    assert to_usd(7) == "$7.00"

    assert to_usd(7.25) == "$7.25"

    assert to_usd(7.2) == "$7.20"

    assert to_usd(7.88888888) == "$7.89"

    assert to_usd(1000000) == "$1,000,000.00"


def test_human_friendly_timestamp():
    d = datetime.datetime(2019, 5, 7, 12, 47, 25)
    assert human_friendly_timestamp(d) == "2019-05-07 12:47 PM"


def test_find_product():
    products = [
        {"id":1, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":5, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":4, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":2, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":3, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    ]

    found_product = find_product(products, 4)

    assert found_product == {"id":4, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25}

    with pytest.raises(IndexError):
        find_product(products, 6)

def test_calculate_total_price():
    products = [
        {"id":1, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":5, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":4, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":2, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":3, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    ]

    selected_ids = [1,3,2]

    assert round(calculate_total_price(products, selected_ids), 2) == 31.48

    assert calculate_total_price([], []) == 0

