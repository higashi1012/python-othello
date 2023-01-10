import unittest
from scripts.for_test import show_board


class TestTashizan(unittest.TestCase):

    def test_tashizan(self):

        expected = None
        actual = show_board()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()