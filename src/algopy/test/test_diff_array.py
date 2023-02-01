import pytest
from algopy.diff_array import diff_array


@pytest.mark.parametrize("input_1, input_2, expected_result", [
    (["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"],
        ["diorite", "andesite", "grass", "dirt", "dead shrub"],
        ["pink wool"]),
    (["andesite", "grass", "dirt", "pink wool", "dead shrub"],
     ["diorite", "andesite", "grass", "dirt", "dead shrub"],
     ["diorite", "pink wool"]),
    (["andesite", "grass", "dirt", "dead shrub"],
        ["grass", "dirt", "andesite", "dead shrub"],
     []),
    ([], ["snuffleupagus", "cookie monster", "elmo"],
     ["cookie monster", "elmo", "snuffleupagus",]),
])
def test_diff_array(input_1, input_2, expected_result):
    assert diff_array(input_1, input_2) == expected_result
