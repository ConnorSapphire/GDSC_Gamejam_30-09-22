import constants
import arcade


class PerfectLine(arcade.Sprite):
    def __init__(self, sprite_path: str, scaling: int) -> None:
        super().__init__(sprite_path, scaling)

        self.center_x = constants.SCREEN_WIDTH / 2
        self.center_y = constants.PERFECT_LINE_Y
        
    def update(self):
        pass