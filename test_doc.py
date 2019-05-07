from shopping_cart.py import *

def test_to_usd():
    assert to_usd(7) == "$7.00"

    assert to_usd(7.25) == "$7.25"

    assert to_usd(7.2) == "$7.20"

    assert to_usd(7.88888888) == "$7.89"

    assert to_usd(1000) == "$1,000.00"