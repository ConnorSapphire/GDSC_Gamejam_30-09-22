import constants
import arcade

from colours import Colours


class Beat:
    def __init__(self, colour: Colours, lane: int) -> None:
        self.lane = lane
        self.colour = colour

        # WARNING magic number
        self.sprite_y = constants.SCREEN_HEIGHT - 40
        self.sprite_x = constants.LANE_START + constants.LANE_SIZE * lane

        self.sprite = arcade.Sprite(colour.value, constants.BEAT_SCALING)
        self.sprite.center_x = self.sprite_x
        self.sprite.center_y = self.sprite_y

    def update(self):
        self.sprite.center_y -= constants.BEAT_SPEED
