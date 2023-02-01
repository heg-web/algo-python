from algopy.multiply import multiply_array, multiply_all, multiply_all_mixed


class TestMultiplyArray:
    def test_empty_array_return_1(self):
        assert multiply_array([]) == 1

    def test_does_multiply_an_array(self):
        assert multiply_array([3, 2]) == 6

    def test_supports_float(self):
        assert multiply_array([-3, 4, 2.5]) == -30


class TestMultiplyAll:
    def test_supports_array_of_array(self):
        assert multiply_all([[1], [2], [3]]) == 6

    def test_supports_array_of_different_lengths(self):
        assert multiply_all([[1, 2], [3, 4], [5, 6, 7]]) == 5040

    def test_works_with_float(self):
        assert multiply_all([[5, 1], [0.2, 4, 0.5], [3, 9]]) == 54


class TestMultiplyAllMixed:
    def test_supports_any_combinasion_of_array_and_any_deepth(self):
        assert multiply_all_mixed([3, [2], [4, [5, [6], 7], 8]]) == 40320

    def test_supports_max_recursion(self):
        arr = [13, 2]
        for i in range(1, 2000):
            arr = [arr, 1]
        assert multiply_all_mixed(arr) == 26
