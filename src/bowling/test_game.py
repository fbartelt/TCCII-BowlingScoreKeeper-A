import unittest

from game import BowlingGame
from frame import Frame


class TestGames(unittest.TestCase):
    def test_score(self):
        game = BowlingGame()
        frames = [[1, 5], [3, 6], [7, 2], [3, 6], [4, 4],
                  [5, 3], [3, 3], [4, 5], [8, 1], [2, 6]]
        for frame in frames:
            fram = Frame(frame[0], frame[1])
            game.add_frame(fram)

        self.assertEqual(game.score(), 81)

    def test_strike(self):
        game = BowlingGame()
        frames = [[10, 0], [3, 6], [7, 2], [3, 6], [4, 4],
                  [5, 3], [3, 3], [4, 5], [8, 1], [2, 6]]
        for frame in frames:
            fram = Frame(frame[0], frame[1])
            game.add_frame(fram)

        self.assertEqual(game.score(), 94)

    def test_spare(self):
        game = BowlingGame()
        frames = [[1, 9], [3, 6], [7, 2], [3, 6], [4, 4],
                  [5, 3], [3, 3], [4, 5], [8, 1], [2, 6]]
        for frame in frames:
            fram = Frame(frame[0], frame[1])
            game.add_frame(fram)

        self.assertEqual(game.score(), 88)

    def test_spare_strike(self):
        game = BowlingGame()
        frames = [[10, 0], [4, 6], [7, 2], [3, 6], [4, 4],
                  [5, 3], [3, 3], [4, 5], [8, 1], [2, 6]]
        for frame in frames:
            fram = Frame(frame[0], frame[1])
            game.add_frame(fram)

        self.assertEqual(game.score(), 103)

    def test_N_strikes(self):
        game = BowlingGame()
        frames = [[10, 0], [10, 0], [7, 2], [3, 6], [4, 4],
                  [5, 3], [3, 3], [4, 5], [8, 1], [2, 6]]
        for frame in frames:
            fram = Frame(frame[0], frame[1])
            game.add_frame(fram)
        
        self.assertEqual(game.score(), 112)


if __name__ == '__main__':
    unittest.main()
