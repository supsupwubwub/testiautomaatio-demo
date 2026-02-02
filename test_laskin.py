import unittest
from laskin import plus

class TestLaskin(unittest.TestCase):
    def test_plus(self):
        # Testataan, että 1 + 1 on 2
        self.assertEqual(plus(1, 1), 2)

if __name__ == '__main__':
    unittest.main()
