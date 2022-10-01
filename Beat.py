from email.policy import default
import arcade
import Colours

LANE_SIZE = 100

class Beat:
    def __init__(self, colour: Colours, lane: int):
        self.lane = lane
        self.colour = colour

        self.sprite_y = 0
        self.sprite_x = LANE_SIZE * lane

        self.sprite = arcade.Sprite(colour.value, 0.5)
        self.sprite.center_x = self.sprite_x
        self.sprite.center_y = self.sprite_y
