from sqlite3 import complete_statement
import constants
import arcade


class Player(arcade.Sprite):
    def __init__(self, sprite_path: str, scaling: int, lane: int) -> None:
        super().__init__(sprite_path, scaling)

        self.lane = lane

        self.sprite_y = constants.PLAYER_START_Y
        self.sprite_x = constants.LANE_START + constants.LANE_SIZE * lane

        # self.sprite = arcade.Sprite(
        #     "./sprites/tmp_player.png", constants.PLAYER_SCALING)
        self.center_x = self.sprite_x
        self.center_y = self.sprite_y

    def change_lane(self, lane: int) -> None:
        if (self.lane + lane) < 0 or (self.lane + lane) > 4:
            return

        self.lane += lane
        self.sprite_x = self.center_x + (constants.LANE_SIZE * lane)
        self.center_x = self.sprite_x

    def update(self) -> None:
        pass