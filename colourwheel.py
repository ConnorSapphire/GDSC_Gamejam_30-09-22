import arcade
import constants

COLOUR_WHEEL_DIM = 512

class ColourWheel(arcade.Sprite):
    def __init__(self, sprite_path: str, scaling: int) -> None:
        super().__init__(sprite_path, scaling)
        self.center_x = constants.SCREEN_WIDTH - COLOUR_WHEEL_DIM * scaling / 2
        self.center_y = constants.SCREEN_HEIGHT - COLOUR_WHEEL_DIM * scaling / 2
    
