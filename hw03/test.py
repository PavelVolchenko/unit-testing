import unittest
from is_even_or_odd import is_even_or_odd
from is_in_interval import is_in_interval


class IsEvenOrOdd(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even_or_odd(8))

    def test_odd(self):
        self.assertFalse(is_even_or_odd(5))


class IsInInterval(unittest.TestCase):
    def test_in_interval(self):
        self.assertTrue(is_in_interval(25))
        self.assertTrue(is_in_interval(100))

    def test_less_then_interval(self):
        self.assertFalse(is_in_interval(24))

    def test_more_than_interval(self):
        self.assertFalse(is_in_interval(101))
