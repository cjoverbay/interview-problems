from solution.ch_01_arrays_and_strings import p_04_MergeSortedArrays
from utils.test import get_implementations
from utils.test import TestCase

# Grab all specific implementations from this solution
to_test = get_implementations(p_04_MergeSortedArrays)


class Tests(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[-1, 0, 3, 4], [-2, 2]], [-2, -1, 0, 2, 3, 4])

    def test_one_empty(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[], [-2, 2]], [-2, 2])

    def test_both_empty(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[], []], [])
