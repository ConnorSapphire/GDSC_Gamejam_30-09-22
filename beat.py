import constants
import arcade

from colours import Colours


class Beat(arcade.Sprite):
    def __init__(self, path: Colours, scaling: int, colour: Colours, lane: int) -> None:
        super().__init__(path.value, scaling)
        self.lane = lane
        self.colour = colour

        # WARNING magic number
        self.sprite_y = constants.SCREEN_HEIGHT - 40
        self.sprite_x = constants.LANE_START + constants.LANE_SIZE * lane

        # self.sprite = arcade.Sprite(colour.value, constants.BEAT_SCALING)
        self.center_x = self.sprite_x
        self.center_y = self.sprite_y

        # self.sprite.velocity = (0, -constants.BEAT_SPEED)

    def update(self):
        # If reaches end of screen
        if self.center_y < constants.SCREEN_HEIGHT - constants.SCREEN_HEIGHT:
            self.kill()

        # Otherwise move down
        self.center_y -= constants.BEAT_SPEED
