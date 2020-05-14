import unittest
from .app import multiply, multiply_short


class TestMultiply(unittest.TestCase):

    def test_basic(self):
        data = [1, 2, 3, 4]
        self.assertListEqual(multiply(data), [24, 12, 8, 6])

    def test_basic_both(self):
        data = [1, 2, 3, 4]
        self.assertListEqual(multiply(data), multiply_short(data))

    def test_empty(self):
        with self.assertRaises(ValueError):
            multiply([])

    def test_type(self):
        with self.assertRaises(ValueError):
            multiply('error')


if __name__ == '__main__':
    unittest.main()
