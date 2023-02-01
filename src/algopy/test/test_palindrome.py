import pytest
from algopy.palindrome import is_palindrome


def test_is_palindrome_simple_test():
    assert is_palindrome("eye")


def test_is_palindrome_simple_not_test():
    assert not is_palindrome("nope")


def test_is_palindrome_almost():
    assert not is_palindrome("almostomla")


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("_eye", True),
    ("race car", True),
    ("A man, a plan, a canal. Panama", True),
    ("Never odd or even", True),
    ('"0_0 (: /- :) 0-0"', True),
    ("1 eye for of 1 eye.", False),
    ("five|_/|four", False),
    ("not a palindrome", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result


def test_is_palindrome_ignores_case():
    assert is_palindrome("My age is 0, 0 si ega ym.")
