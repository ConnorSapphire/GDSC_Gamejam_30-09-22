from calendar import different_locale
import constants
import arcade
import math

from colours import Colours


class Beat(arcade.Sprite):
    def __init__(self, path: Colours, scaling: int, colour: Colours, lane: int) -> None:
        super().__init__(path.value, scaling)
        self.lane = lane
        self.colour = colour

        # WARNING magic number
        self.sprite_y = constants.SCREEN_HEIGHT - 20
        self.sprite_x = constants.LANE_START + constants.LANE_SIZE * lane

        # self.sprite = arcade.Sprite(colour.value, constants.BEAT_SCALING)
        self.center_x = self.sprite_x
        self.center_y = self.sprite_y

        # self.sprite.velocity = (0, -constants.BEAT_SPEED)

    def hit(self):
        if (self.center_y <= constants.PERFECT_LINE_Y + (constants.BEAT_HEIGHT / 2) and self.center_y >= constants.PERFECT_LINE_Y - (constants.BEAT_HEIGHT / 2)):
            difference = abs(self.center_y - constants.PERFECT_LINE_Y)
            segment_length = (constants.BEAT_HEIGHT / 2) / constants.PERFECT_SCORE
            score = abs(math.floor(difference / segment_length) - constants.PERFECT_SCORE)
            # Return no from 1 - 5 (5 being dead center, 1 being outer edge)
            # NB - will return 0 if the very edge pixel is hit
            return score
        else:
            self.kill()
            return 0

    def update(self):
        # If reaches end of screen
        if self.center_y < 0:
            self.kill()

        # Otherwise move down
        self.center_y -= constants.BEAT_SPEED

    # def move(self, crotchet_legnth)
    #     # If reaches end of screen
    #     if self.center_y < 0:
    #         self.kill()

    #     # Otherwise move down
    #     self.center_y -= crotchet_legnth
