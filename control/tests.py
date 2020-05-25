import unittest
from .app import multiply, multiply_short, mocking, multiply_linear_time
from unittest.mock import patch


class TestMultiply(unittest.TestCase):

    def test_basic(self):
        data = [1, 2, 3, 4]
        self.assertListEqual(multiply(data), [24, 12, 8, 6])

    def test_basic_both(self):
        data = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(multiply(data), multiply_linear_time(data))
        self.assertListEqual(multiply(data), multiply_short(data))

    def test_empty(self):
        with self.assertRaises(ValueError):
            multiply([])

    def test_type(self):
        with self.assertRaises(ValueError):
            multiply('error')

    def test_zeros(self):
        with self.assertRaises(ValueError):
            multiply_linear_time([0, 1, 2, 3])

    @patch('control.app.multiply', return_value=[i for i in range(10_000_000)])
    def test_large(self, input):
        self.assertListEqual(mocking(),
                             [i for i in range(10_000_000)])


if __name__ == '__main__':
    unittest.main()
