import unittest
import doctest

import solution


def run_tests():
    print('Loading Tests...')
    loader = unittest.TestLoader()
    suite = loader.discover('test')

    print('Running Unit Tests...')
    runner = unittest.TextTestRunner(None, True, 5)
    runner.run(suite)

    print('Running Doc Tests...')
    print_functions(solution)
    print_functions(solution.ch_01_arrays_and_strings)
    doctest.testmod(solution)


def print_functions(module):
    print([d for d in dir(module) if '__' not in d])


if __name__ == '__main__':
    run_tests()

