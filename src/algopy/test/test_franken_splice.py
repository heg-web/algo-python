from algopy.franken_splice import franken_splice


def test_franken_splice_with_ints_1():
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert franken_splice(a, b, 1) == [4, 1, 2, 3, 5, 6] and a == [1, 2, 3] and b == [4, 5, 6]


def test_franken_splice_with_ints_2():
    assert franken_splice([1, 2, 3], [4, 5], 1) == [4, 1, 2, 3, 5]


def test_franken_splice_with_strings_1():
    assert franken_splice(
        ["claw", "tentacle"],
        ["head", "shoulders", "knees", "toes"],
        2
    ) == ["head", "shoulders", "claw", "tentacle", "knees", "toes"]


def test_franken_splice_with_mixed_content():
    assert franken_splice([1, 2], ["a", "b"], 1) == ["a", 1, 2, "b"]
