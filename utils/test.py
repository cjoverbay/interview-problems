import unittest

def get_implementations(package):
    implementations = []
    for attr in [getattr(package, x) for x in dir(package)]:
        if callable(attr):
            implementations.append(attr)

    return implementations


class TestCase(unittest.TestCase):
    # Custom assert which logs function name on an error.
    # (To determine which implementation caused error)
    def assertFunctionResultEquals(self, func, params, expected):
        return self.assertEqual(expected, func(*params), 'in function ' + func.__name__)
