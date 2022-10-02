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

    def score(self) -> int:
        '''Score the beat center's proximity to the line. If the center of the beat is on the line return 5, incrementally return less the further towards the edge the beat
        is. Returning 0 if only the very circumference of the beat is touching the line.'''
        difference = abs(self.center_y - constants.PERFECT_LINE_Y)
        segment_length = (constants.BEAT_HEIGHT / 2) / constants.PERFECT_SCORE
        score = abs(math.floor(difference / segment_length) - constants.PERFECT_SCORE)
        return score

    def hit(self, colour: int) -> int:
        '''Determine if the beat is on the line and the right colour combination was pressed. Return the score out of 5.'''
        if (self.center_y <= constants.PERFECT_LINE_Y + (constants.BEAT_HEIGHT / 2) and self.center_y >= constants.PERFECT_LINE_Y - (constants.BEAT_HEIGHT / 2)):
            if (self.colour == Colours.BLUE and colour == constants.BLUE):
                score = self.score()
                self.kill()
                return score
            elif (self.colour == Colours.YELLOW and colour == constants.YELLOW):
                score = self.score()
                self.kill()
                return score
            elif (self.colour == Colours.RED and colour == constants.RED):
                score = self.score()
                self.kill()
                return score
            elif (self.colour == Colours.GREEN and colour == constants.GREEN):
                score = self.score()
                self.kill()
                return score
            elif (self.colour == Colours.PURPLE and colour == constants.PURPLE):
                score = self.score()
                self.kill()
                return score
            elif (self.colour == Colours.ORANGE and colour == constants.ORANGE):
                score = self.score()
                self.kill()
                return score
            elif (self.colour == Colours.BROWN and colour == constants.BROWN):
                score = self.score()
                self.kill()
                return score
            else:
                self.kill()
                return 0
        else:
            return 0

    def update(self) -> None:
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
