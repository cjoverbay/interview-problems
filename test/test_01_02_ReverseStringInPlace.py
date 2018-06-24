from solution.ch_01_arrays_and_strings import p_02_ReverseStrings
from utils.test import get_implementations
from utils.test import TestCase

# Grab all specific implementations from this solution
to_test = get_implementations(p_02_ReverseStrings)


class Tests(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [['a', 'b', 'c', 'd']], ['d', 'c', 'b', 'a'])

    def test_odd_length(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [['a', 'b', 'c']], ['c', 'b', 'a'])

    def test_empty(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[]], [])