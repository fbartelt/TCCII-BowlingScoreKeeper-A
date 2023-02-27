from typing import List

from frame import Frame
from functools import reduce


class BowlingGame:
    frames: List[Frame] = []
    bonus: Frame

    def __init__(self):
        self.frames = []

    def add_frame(self, frame: Frame):
        """ Add a frame to the game """
        if len(self.frames) < 10:
            self.frames.append(frame)

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        # To be implemented
        pass

    def score(self) -> int:
        """ Get the score from the game """
        score = 0
        for i, frame in enumerate(self.frames):    
            score += frame.score() 
            if frame.is_strike():
                score += self._strike(self.frames[i+1::])
                # score += self.frames[i+1].score()
                # strikes.append(i)
            elif frame.is_spare():
                score += self.frames[i+1].first_throw
            print(score)
            

        return score
    
    def _strike(self, sub_frames):
        if sub_frames[0].is_strike():
            return sub_frames[0].score() + self._strike(sub_frames[1::])
        else:
            return sub_frames[0].score()


    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        # To be implemented
        pass
