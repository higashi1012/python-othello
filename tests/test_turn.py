import unittest
from scripts.for_test import turn


class TestTashizan(unittest.TestCase):

    def test_tashizan(self):

        expected = None
        actual = turn()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()