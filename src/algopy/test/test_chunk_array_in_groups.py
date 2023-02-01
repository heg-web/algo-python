from algopy.chunk_array_in_groups import chunk_array_in_groups


def test_chunk_array_in_groups_with_strings():
    assert chunk_array_in_groups(["a", "b", "c", "d"], 2) == [
        ["a", "b"],
        ["c", "d"]
    ]


def test_chunk_array_in_groups_with_numbers():
    assert chunk_array_in_groups([0, 1, 2, 3, 4, 5], 3) == [
        [0, 1, 2],
        [3, 4, 5]
    ]


def test_chunk_array_in_groups_with_numbers2():
    assert chunk_array_in_groups([0, 1, 2, 3, 4, 5], 2) == [
        [0, 1],
        [2, 3],
        [4, 5]
    ]


def test_chunk_array_in_groups_with_remainder_of_division_1():
    assert chunk_array_in_groups([0, 1, 2, 3, 4, 5], 4) == [
        [0, 1, 2, 3],
        [4, 5]
    ]


def test_chunk_array_in_groups_with_remainder_of_division_2():
    assert chunk_array_in_groups([0, 1, 2, 3, 4, 5, 6], 3) == [
        [0, 1, 2],
        [3, 4, 5],
        [6]
    ]


def test_chunk_array_in_groups_with_remainder_of_division_3():
    assert chunk_array_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4) == [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8]
    ]


def test_chunk_array_in_groups_with_remainder_of_division_4():
    assert chunk_array_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2) == [
        [0, 1],
        [2, 3],
        [4, 5],
        [6, 7],
        [8]
    ]
