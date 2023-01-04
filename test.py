import unittest
from script import load_exponent


class TestLoadExponentMethod(unittest.TestCase):
    def test_incorrect_args(self):
        with self.assertRaises(TypeError):
            load_exponent("5.1", "7")

    def test_without_args(self):
        with self.assertRaises(TypeError):
            load_exponent()

    def test_check_result(self):
        self.assertEqual(load_exponent(9, 3), 72)


if __name__ == "__main__":
    unittest.main()
