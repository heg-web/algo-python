from algopy.find_secret import find_secret


def test_find_secret_1():
    assert find_secret({
        "start": {
            "name": "abc",
            "params": [2, 6]
        },
        "abc": lambda a, b: a // b,
        "names": ["a", "b", "c", "d"]
    }) == "d"


def test_find_secret_2():
    assert find_secret({
        "start": {
            "name": "bac",
            "params": [1, 2]
        },
        "bac": lambda a, b: a,
        "names": ["a", "b", "c", "d"]
    }) == "c"
