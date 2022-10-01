import game_constants
import arcade

class Player:
    def __init__(self, lane: int) -> None:
        self.lane = lane

        # WARNING magic number
        self.sprite_y = 40
        self.sprite_x = game_constants.LANE_START + game_constants.LANE_SIZE * lane

        self.sprite = arcade.Sprite("./sprites/tmp_player.png", game_constants.PLAYER_SCALING)
        self.sprite.center_x = self.sprite_x
        self.sprite.center_y = self.sprite_y