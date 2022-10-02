import constants
import arcade
import random
from colours import Colours
from beat import Beat
from typing import List

class BeatManager:
    def __init__(self):
        pass

    def draw_lanes(self):
        for i in range(constants.NUM_LANES + 1):
            # Calculate x position for current lane line
            x = constants.LANE_START + constants.LANE_SIZE * i - constants.LANE_SIZE / 2
            # Draw lane line
            arcade.draw_line(x, 0, x, constants.SCREEN_HEIGHT, arcade.color.BLACK, 2)

    # def create_perfect_line(self):
    #     print(arcade.draw_line(constants.LANE_START, constants.PERFECT_LINE_Y, 600, constants.PERFECT_LINE_Y, arcade.color.BLACK, 2))
        # arcade.draw_line(constants.LANE_START, constants.PERFECT_LINE_Y, constants.LANE_END, constants.PERFECT_LINE_Y, arcade.color.BLACK, 2)
        # arcade.draw_line(0, constants.PERFECT_LINE_Y, constants.SCREEN_WIDTH, constants.PERFECT_LINE_Y, arcade.color.RED, 5)

    def create_beat(self, colour, lane):
        return Beat(Colours.BLUE, 1, colour, lane)


    def update(self, conductor, beat_info):
        # print(conductor.song_position)
        # print(conductor.timing)

        if conductor.song_position >= conductor.timing:
            print("DSJNKJDFDFKNSJDKNSJDKJN")
            beat_to_add = self.create_beat(beat_info[0], beat_info[1])
            # self.scene.add_sprite(constants.BEAT_LAYER, beat_to_add)
            return beat_to_add