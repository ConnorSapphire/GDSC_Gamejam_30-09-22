import game_constants
import arcade

from Colours import Colours


class Beat:
    def __init__(self, colour: Colours, lane: int) -> None:
        self.lane = lane
        self.colour = colour

        # WARNING magic number
        self.sprite_y = game_constants.SCREEN_HEIGHT - 40
        self.sprite_x = game_constants.LANE_START + game_constants.LANE_SIZE * lane

        self.sprite = arcade.Sprite(colour.value, game_constants.BEAT_SCALING)
        self.sprite.center_x = self.sprite_x
        self.sprite.center_y = self.sprite_y