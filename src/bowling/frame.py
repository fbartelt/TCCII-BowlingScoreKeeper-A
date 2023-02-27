class Frame:
    def __init__(self, first_throw: int, second_throw: int) -> None:
        self.first_throw = first_throw
        self.second_throw = second_throw

    def score(self) -> int:
        """ The score of a single frame """
        return self.first_throw + self.second_throw

    def is_strike(self) -> bool:
        """ Return whether the frame is a strike or not """
        return (self.first_throw == 10) or (self.second_throw == 10)

    def is_spare(self) -> bool:
        """ Return whether the frame is a spare or not """
        return (not self.is_strike()) and (self.score() == 10)

    def is_last_frame(self) -> bool:
        """ Return whether the frame is a last frame of the game """
        # To be implemented
        pass

    def bonus(self) -> int:
        """ Bonus throw """
        # To be implemented
        pass
