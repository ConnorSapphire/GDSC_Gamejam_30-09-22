from enum import Enum

class Colours(Enum):
    """
    Enum for colours of the beats. The value contains it's sprite path
    """
    RED = "./sprites/red_beat.png"
    BLUE = "./sprites/blue_beat.png"
    GREEN = "./sprites/green_beat.png"

    YELLOW = "./sprites/yellow_beat.png"
    MAGENTA = "./sprites/purple_beat.png"
    CYAN = "./sprites/cyan_beat.png"

# DEPRACATED
# Colour mixing algorithm using the reverse-bayesan type formula
# https://stackoverflow.com/questions/1351442/is-there-an-algorithm-for-color-mixing-that-works-like-mixing-real-colors
# NewColor.R = (Color1.R * Color2.R)/255
# NewColor.G = (Color1.G * Color2.G)/255
# NewColor.B = (Color1.B * Color2.B)/255
