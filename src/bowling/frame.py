class Frame:
    def __init__(self, first_throw: int, second_throw: int) -> None:
        self.first_throw = first_throw
        self.second_throw = second_throw

    def score(self) -> int:
        """ The score of a single frame """
        # To be implemented
        pass

    def is_strike(self) -> bool:
        """ Return whether the frame is a strike or not """
        # To be implemented
        pass

    def is_spare(self) -> bool:
        """ Return whether the frame is a spare or not """
        # To be implemented
        pass

    def is_last_frame(self) -> bool:
        """ Return whether the frame is a last frame of the game """
        # To be implemented
        pass

    def bonus(self) -> int:
        """ Bonus throw """
        # To be implemented
        pass
