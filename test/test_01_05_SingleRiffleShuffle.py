from solution.ch_01_arrays_and_strings import p_05_SingleRiffleShuffle
from utils.test import get_implementations
from utils.test import TestCase

# Grab all specific implementations from this solution
to_test = get_implementations(p_05_SingleRiffleShuffle)


class Tests(TestCase):
    def setUp(self):
        pass

    def test_faro_shuffle(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[1, 3], [2, 4], [1, 2, 3, 4]], True)

    def test_non_faro_shuffle(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[1, 3], [2, 4], [1, 2, 4, 3]], True)

    def test_spectator_shuffle(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[1, 3], [2, 4], [1, 4, 2, 3]], False)

    def test_one_empty(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[], [2, 4], [2, 4]], True)

    def test_all_empty(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[], [], []], True)

    def test_incorrect_len(self):
        for implementation in to_test:
            self.assertFunctionResultEquals(implementation, [[1, 3, 5], [2, 4], [1, 2, 3, 4]], False)
