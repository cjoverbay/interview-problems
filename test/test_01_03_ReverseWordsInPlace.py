from solution.ch_01_arrays_and_strings import p_03_ReverseWords
from utils.test import get_implementations
from utils.test import TestCase

# Grab all specific implementations from this solution
to_test = get_implementations(p_03_ReverseWords)


class Tests(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [['a', 'b', ' ', 'd']], ['d', ' ', 'a', 'b'])

    def test_odd_length(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [['a', 'b', 'c']], ['a', 'b', 'c'])

    def test_long(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[*'like to mine']], [*'mine to like'])

    def test_end_in_space(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[*'roses have thorns ']], [*' thorns have roses'])

    def test_empty(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[]], [])