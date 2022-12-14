
"""
@from https://api.arcade.academy/en/latest/examples/starting_template.html#starting-template
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
from cgi import test
import random
import string
import arcade
import constants
from beat import Beat
from colours import Colours
from player import Player
from beat_manager import BeatManager
from perfect_line import PerfectLine
from conductor import Conductor
from colourwheel import ColourWheel
from user_interface import UserInterface

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width: int, height: int, title: string) -> None:
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # Scene
        self.scene = None

        # Physics/movement
        self.physics_engine = None

        #background
        self.background = None

    def setup(self) -> None:
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        self.beatmap = {5:(Colours.BLUE, 3), 7:(Colours.RED, 2),
                        8:(Colours.YELLOW, 1), 9:(Colours.YELLOW, 1),
                        10:(Colours.BLUE, 4), 11:(Colours.RED, 3),
                        12:(Colours.YELLOW, 2),
                        13:(Colours.GREEN, 0), 15:(Colours.PURPLE, 1),
                        17:(Colours.ORANGE, 2), 19:(Colours.BROWN, 4), 
                        20:(Colours.RED, 0), 21:(Colours.BLUE, 4), 
                        22:(Colours.YELLOW, 2), 23:(Colours.BROWN, 2),
                        24:(Colours.RED, 0), 25:(Colours.ORANGE, 0), 
                        26:(Colours.BLUE, 4), 27:(Colours.PURPLE, 4), 
                        28:(Colours.YELLOW, 2), 29:(Colours.GREEN, 2), 
                        30:(Colours.BROWN, 1), 31:(Colours.BROWN, 3), 
                        32:(Colours.ORANGE, 0), 33:(Colours.PURPLE, 1), 
                        34:(Colours.ORANGE, 4), 35:(Colours.GREEN, 3), 
                        36:(Colours.RED, 2), 37:(Colours.YELLOW, 2), 
                        38:(Colours.BLUE, 2), 39:(Colours.BROWN, 2)}

        # Logic management
        self.beat_manager = BeatManager()

        # Scene
        self.scene = arcade.Scene()
        self.scene.add_sprite_list(constants.PLAYER_LAYER)
        self.scene.add_sprite_list(constants.BEAT_LAYER, use_spatial_hash=True)
        self.scene.add_sprite_list(constants.PERFECT_LINE_LAYER, use_spatial_hash=True)
        self.scene.add_sprite_list(constants.UI_LAYER, use_spatial_hash=True)

        # Colour wheel
        self.colour_wheel = ColourWheel("./sprites/colour_wheel.png", 0.1)
        self.scene.add_sprite(constants.UI_LAYER, self.colour_wheel)

        # Player setup
        self.player = Player(constants.BLUE_PLAYER, constants.PLAYER_SCALING, 3)
        self.scene.add_sprite(constants.PLAYER_LAYER, self.player)

        # Perfect line
        self.perfect_line = PerfectLine("./sprites/perfect_line.png", constants.PERFECT_LINE_SCALING)
        self.scene.add_sprite(constants.PERFECT_LINE_LAYER, self.perfect_line)

        # Tutorial
        self.user_interface = UserInterface()
        
        #Background
        self.background = arcade.load_texture("./background.png")



        # Testing area
        self.conductor = Conductor()
        self.conductor.set_song(arcade.Sound("music/clappingtrio.wav", streaming=True))
        # change this eventually to some sort of file reading system
        self.conductor.set_bpm(117.0)
        self.conductor.set_offset(1.0)

        # Physics engine
        # NOTE has to go after everything else is initialised
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player, self.scene.get_sprite_list(constants.BEAT_LAYER))

        self.beat_manager = BeatManager()

        self.conductor.play()

        self.created = False
        self.read = 0

        # Key inputs
        self.hit_colour = 0
        self.wait_time = 0
        self.is_wait = False

        # Scoring
        self.score = 0
        self.hit_score = -1
        self.score_comment_timer = 0

    def on_draw(self) -> None:
        """
        Render the screen.
        """
        # Clears the previous frame
        self.clear()

        # Call draw() on all your sprite lists below

        #Draw Background
        arcade.draw_lrwh_rectangle_textured(0, 0,constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)

        #Draws the score
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, constants.SCREEN_HEIGHT-20, arcade.color.WHITE, 20, font_name="Kenney Pixel")


        # Draws the lanes for the beats to spawn in

        self.beat_manager.draw_lanes()
        #NOTE disabling for now -- aim to replace with a sprite
        # self.beat_manager.draw_perfect_line()
        self.scene.draw()

        if (self.user_interface.tutorial_done == False):
            self.user_interface.tutorial()
        elif self.hit_score >= 0:
            self.display_score_comment()


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        # Determine if multiple keys are pressed
        if (self.is_wait):
            self.wait_time += 1
        beats = self.scene.get_sprite_list("Beats")
        if (self.wait_time >= constants.KEYSTROKE_WAIT):
            self.wait_time = 0
            self.is_wait = False
            # if (self.hit_colour == constants.RED):
            #     lane = self.player.lane
            #     self.player = Player(constants.RED_PLAYER, constants.PLAYER_SCALING, lane)
            beats_in_lane = list(())
            for beat in beats:
                if (beat.lane == self.player.lane):
                    beats_in_lane.append(beat)
            hit_score = 0
            for beat in beats_in_lane:
                hit_score += beat.hit(self.hit_colour)
            self.score += hit_score
            self.hit_score = hit_score
            self.hit_colour = 0
        
        # Update scene including all beats and player
        self.scene.update()
        self.conductor.update_song_position()
        # self.physics_engine.update()

        # print(self.conductor.song_position)
        # print(self.conductor.timing)

        if self.read < self.conductor.beat_counter:
            self.created = False

        beat_info = self.read_beatmap(self.beatmap)
        if beat_info is not None:
            new_beat = self.beat_manager.update(self.conductor, self.read_beatmap(self.beatmap))

            if new_beat is not None and not self.created:
                self.scene.add_sprite(constants.BEAT_LAYER, new_beat)
                self.created = True

            beat_info = None

    def display_score_comment(self):
        score_comment = ""
        if self.hit_score == 5:
            score_comment = "PERFECT!!!"
        elif self.hit_score == 4:
            score_comment = "Amazing!"
        elif self.hit_score == 3:
            score_comment = "Well Done!"
        elif self.hit_score == 2:
            score_comment = "Nice"
        elif self.hit_score == 1:
            score_comment = "Acceptable"
        elif self.hit_score == 0:
            score_comment = "MISS"
        arcade.draw_text(score_comment, constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, arcade.color.WHITE, 30, font_name="Kenney Pixel", anchor_x="center", anchor_y="center")
        self.score_comment_timer += 1
        if (self.score_comment_timer >= constants.SCORE_COMMENT_WAIT):
            self.hit_score = -1
            self.score_comment_timer = 0

    def read_beatmap(self, beatmap):
        if self.conductor.beat_counter in beatmap:
            self.conductor.set_new_note_timing(self.conductor.beat_counter)
            self.read = self.conductor.beat_counter
            return self.beatmap.get(self.conductor.beat_counter)

        return None


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.LEFT:
            self.player.change_lane(-1)
        elif key == arcade.key.RIGHT:
            self.player.change_lane(1)
        if key == arcade.key.A:
            self.hit_colour += constants.BLUE
            self.is_wait = True
        if key == arcade.key.S:
            self.hit_colour += constants.YELLOW
            self.is_wait = True
        if key == arcade.key.D:
            self.hit_colour += constants.RED
            self.is_wait = True
        


    # def on_key_release(self, key, modifiers):
    #     """Called when the user releases a key."""

    #     if key == arcade.key.UP or key == arcade.key.W:
    #         pass
    #     elif key == arcade.key.DOWN or key == arcade.key.S:
    #         pass
    #     elif key == arcade.key.LEFT or key == arcade.key.A:
    #         pass
    #     elif key == arcade.key.RIGHT or key == arcade.key.D:
    #         pass


    # def beat_in_lane(lane, beats) -> Beat:
    #     """ Checks if any beats are in a given lane and returns the first one"""

    #     for beat in beats:
    #         if beat.lane == lane:
    #             return beat
    #     return None

def main() -> None:
    """ Main function """
    game = MyGame(constants.SCREEN_WIDTH,
                  constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    game.setup()
    game.set_update_rate(1/constants.FPS)
    arcade.run()


if __name__ == "__main__":
    main()
