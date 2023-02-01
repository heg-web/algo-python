import pytest
from algopy.my_replace import my_replace


@pytest.mark.parametrize("text, before, after, expected_result", [
    ("Let us go to the store", "store", "mall", "Let us go to the mall"),
    ("This has a spellngi error", "spellngi",
     "spelling", "This has a spelling error"),
    ("A quick brown fox jumped over the lazy dog", "jumped",
     "leaped", "A quick brown fox leaped over the lazy dog"),
    ("He is Sleeping on the couch", "Sleeping",
     "sitting", "He is Sitting on the couch"),
    ("His name is Tom", "Tom", "john", "His name is John"),
    ("Let us get back to more Coding", "Coding",
     "algorithms", "Let us get back to more Algorithms"),
])
def test_my_replace(text, before, after, expected_result):
    assert my_replace(text, before, after) == expected_result
