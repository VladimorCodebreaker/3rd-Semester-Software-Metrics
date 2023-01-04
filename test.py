"""Implementation of the Test Cases for the function 'load_exponent' - SW Metrics Exam - Part 2"""
import unittest
from script import load_exponent


class TestLoadExponentMethod(unittest.TestCase):
    """Test 'load_exponent' method"""

    def test_incorrect_args(self):
        """Test function with incorrect arguments"""
        with self.assertRaises(TypeError):
            load_exponent("5.1", "7")

    def test_without_args(self):
        """Test function without arguments"""
        with self.assertRaises(TypeError):
            load_exponent()

    def test_check_result(self):
        """Test the result of the function"""
        self.assertEqual(load_exponent(9, 3), 72)

    def test_boolean_args(self):
        """Test function with boolean arguments"""
        with self.assertRaises(TypeError):
            load_exponent(True, False)


if __name__ == "__main__":
    unittest.main()
