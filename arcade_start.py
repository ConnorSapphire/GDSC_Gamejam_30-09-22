
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

        # Physics engine
        # NOTE has to go after everything else is initialised
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player, self.scene.get_sprite_list("Beats"))

        self.beat_manager = BeatManager()

        # Key inputs
        self.hit_colour = 0
        self.wait_time = 0
        self.is_wait = False

        # Scoring
        self.score = 0

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
        # Determine if multiple keys are pressed
        if (self.is_wait):
            self.wait_time += 1
        beats = self.scene.get_sprite_list("Beats")
        if (self.wait_time >= constants.KEYSTROKE_WAIT):
            self.wait_time = 0
            self.is_wait = False
            # TODO check beat in lane:
            beats_in_lane = list(())
            for beat in beats:
                if (beat.lane == self.player.lane):
                    beats_in_lane.append(beat)
            hit_score = 0
            for beat in beats_in_lane:
                hit_score += beat.hit(self.hit_colour)
            self.score += hit_score
            self.hit_colour = 0
        
        # Update scene including all beats and player
        self.scene.update()
        # self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.LEFT:
            self.player.change_lane(-1)
        elif key == arcade.key.RIGHT:
            self.player.change_lane(1)
        if key == arcade.key.A:
            self.hit_colour += 1
            self.is_wait = True
        if key == arcade.key.S:
            self.hit_colour += 2
            self.is_wait = True
        if key == arcade.key.D:
            self.hit_colour += 3
            self.is_wait = True
        


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


def main():
    """ Main function """
    game = MyGame(constants.SCREEN_WIDTH,
                  constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    game.setup()
    game.set_update_rate(1/constants.FPS)
    arcade.run()


if __name__ == "__main__":
    main()
