import constants
import arcade
from colours import Colours
from beat import Beat
from typing import List

class BeatManager:
    def __init__(self) -> None:
        pass

    def draw_lanes(self) -> None:
        for i in range(constants.NUM_LANES + 1):
            # Calculate x position for current lane line
            x = constants.LANE_START + constants.LANE_SIZE * i - constants.LANE_SIZE / 2
            # Draw lane line
            arcade.draw_line(x, 0, x, constants.SCREEN_HEIGHT, arcade.color.BLACK, 2)

    def draw_perfect_line(self) -> None:
        arcade.draw_line(0, constants.PERFECT_LINE_Y, constants.SCREEN_WIDTH, constants.PERFECT_LINE_Y, arcade.color.RED, 5)

    def create_beat(self, colour: Colours, lane: int) -> None:
        return Beat(colour, 1, colour, lane)