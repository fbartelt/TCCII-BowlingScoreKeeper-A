import unittest
from frame import Frame


class TestFrames(unittest.TestCase):
    def test_valid(self):
        frame = Frame(2, 4)
        self.assertTrue(0 <= frame.first_throw + frame.second_throw <= 10)
    
    def test_score(self):
        frame = Frame(2, 6)
        self.assertEqual(frame.score(), 8)
    
    def test_strike(self):
        frame = Frame(10, 0)
        self.assertTrue(frame.is_strike())
        frame = Frame(0, 10)
        self.assertTrue(frame.is_strike())
        frame = Frame(0, 10)
        self.assertFalse(frame.is_spare())

    def test_spare(self):
        frame = Frame(6, 4)
        self.assertTrue(frame.is_spare())
        frame = Frame(4, 6)
        self.assertTrue(frame.is_spare())
        frame = Frame(0, 10)
        self.assertFalse(frame.is_spare())
        


if __name__ == '__main__':
    unittest.main()

# %%
