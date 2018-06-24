from solution.ch_01_arrays_and_strings import p_01_MergeMeetingTimes
from utils.test import get_implementations
from utils.test import TestCase

# Grab all specific implementations from this solution
to_test = get_implementations(p_01_MergeMeetingTimes)


class Tests(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]], [(0, 1), (3, 8), (9, 12)])

    def test_adjacent_merges(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[(1, 2), (2, 3)]], [(1, 3)])

    def test_contained_merges(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[(1, 5), (2, 3)]], [(1, 5)])
