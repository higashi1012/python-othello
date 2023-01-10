import unittest
from othello import playable


class TestTashizan(unittest.TestCase):

    def test_tashizan(self):

        expected = [(2, 3), (3, 2), (4, 5), (5, 4)]
        actual = playable()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()