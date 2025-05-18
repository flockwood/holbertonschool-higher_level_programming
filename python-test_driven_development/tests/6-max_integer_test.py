#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test a list with ordered integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list with unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_sign_numbers(self):
        """Test a list with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)

    def test_floats_and_integers(self):
        """Test a list with both floats and integers."""
        self.assertEqual(max_integer([1.5, 2, 3.5, 2.1]), 3.5)

    def test_max_at_start(self):
        """Test a list where the maximum is the first element."""
        self.assertEqual(max_integer([5, 1, 3, 2]), 5)

    def test_max_at_end(self):
        """Test a list where the maximum is the last element."""
        self.assertEqual(max_integer([1, 3, 2, 6]), 6)

    def test_all_equal(self):
        """Test a list where all elements are the same."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_non_numeric_types(self):
        """Test lists with non-numeric types
        (not necessarily needed but for robustness)."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])


if __name__ == "__main__":
    unittest.main()
