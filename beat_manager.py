import constants
import arcade
from colours import Colours
from beat import Beat
from typing import List

class BeatManager:
    def __init__(self):
        pass

    def draw_lanes(self):
        for i in range(constants.NUM_LANES + 1):
            x = constants.LANE_START + constants.LANE_SIZE * i - constants.LANE_SIZE / 2
            arcade.draw_line(x, 0, x, constants.SCREEN_HEIGHT,
                             arcade.color.BLACK, 2)

    def create_beat(self, colour, lane):
        return Beat(Colours.BLUE, 1, colour, lane)