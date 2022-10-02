
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
import arcade
import constants
from beat import Beat
from colours import Colours
from player import Player
from beat_manager import BeatManager
from conductor import Conductor


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # Scene
        self.scene = None

        # Physics/movement
        self.physics_engine = None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        # Logic management
        self.beat_manager = BeatManager()

        # Scene
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Beats", use_spatial_hash=True)

        # Player setup
        self.player = Player("./sprites/tmp_player.png", constants.PLAYER_SCALING, 3)
        self.scene.add_sprite("Player", self.player)

        # Testing area

        # Testing initial random seleciton of beats
        for i in range(3):
            # Lanes indexed at 0
            beat_to_add = self.beat_manager.create_beat(Colours.BLUE, random.randint(0, constants.NUM_LANES - 1))
            self.scene.add_sprite("Beats", beat_to_add)

        self.conductor = Conductor()
        self.conductor.set_song(arcade.Sound("music/clappingtrio.wav", streaming=True))
        # change this eventually to some sort of file reading system
        self.conductor.set_bpm(117.0) 

        # Physics engine
        # NOTE has to go after everything else is initialised
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player, self.scene.get_sprite_list("Beats"))

        self.beat_manager = BeatManager()

        self.conductor.play()



    def on_draw(self):
        """
        Render the screen.
        """
        # Clears the previous frame
        self.clear()

        # Call draw() on all your sprite lists below

        # Draws the lanes for the beats to spawn in
        self.beat_manager.draw_lanes()
        self.beat_manager.draw_perfect_line()
        self.scene.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        self.scene.update()
        # self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        beats = self.scene.get_sprite_list("Beats")

        # NOTE up and down should be mechanic keys -- grab and combine colours
        if key == arcade.key.UP or key == arcade.key.W:
            if (beats.__len__() > 0):
                hit_beat = beat_in_lane(self, self.player.lane, beats)
                if hit_beat is not None:
                    beats.remove(hit_beat)
                    hit_score = hit_beat.hit()
                    if (hit_score > 0):
                        # TODO increase bucket and record hit score to calculate overall score out of five at end of round
                        pass

        elif key == arcade.key.DOWN or key == arcade.key.S:
            if (beats.__len__() > 0):
                hit_beat = beat_in_lane(self, self.player.lane, beats)
                if hit_beat is not None:
                    beats.remove(hit_beat)
                    hit_score = hit_beat.hit()
                    if (hit_score > 0):
                        # TODO increase bucket and record hit score to calculate overall score out of five at end of round
                        pass

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_lane(-1)

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_lane(1)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            pass
        elif key == arcade.key.DOWN or key == arcade.key.S:
            pass
        elif key == arcade.key.LEFT or key == arcade.key.A:
            pass
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            pass


def beat_in_lane(self, lane, beats) -> Beat:
    """ Checks if any beats are in a given lane and returns the first one"""

    for beat in beats:
        if beat.lane == lane:
            return beat
    return None


def main():
    """ Main function """
    game = MyGame(constants.SCREEN_WIDTH,
                  constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    game.setup()
    game.set_update_rate(1/constants.FPS)
    arcade.run()


if __name__ == "__main__":
    main()
