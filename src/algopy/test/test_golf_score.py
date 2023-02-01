import pytest
from algopy.golf_score import golf_score_to_text


@pytest.mark.parametrize("par, strokes, expected_result", [
    (4, 1, "Hole-in-one!"),
    (4, 2, "Eagle"),
    (5, 2, "Eagle"),
    (4, 3, "Birdie"),
    (4, 4, "Par"),
    (1, 1, "Hole-in-one!"),
    (5, 5, "Par"),
    (4, 5, "Bogey"),
    (4, 6, "Double Bogey"),
    (4, 7, "Go Home!"),
    (5, 9, "Go Home!"),
])
def test_golf_score_to_text(par, strokes, expected_result):
    assert golf_score_to_text(par, strokes) == expected_result
