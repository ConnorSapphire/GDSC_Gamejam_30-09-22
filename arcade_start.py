
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
        # If you have sprite lists, you should create them here,
        # and set them to None

        arcade.set_background_color(arcade.color.AMAZON)

        # Scene
        self.scene = None

        # Physics/movement
        self.physics_engine = None

        self.beat_manager = BeatManager()

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        # Scene
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Beats", use_spatial_hash=True)

        # Player setup
        self.player = Player(3)
        self.scene.add_sprite("Player", self.player.sprite)

        # Testing area

        # Testing initial random seleciton of beats
        for i in range(3):
            self.scene.add_sprite("Beats", self.beat_manager.create_beat(
                Colours.BLUE, random.randint(1, constants.NUM_LANES)).sprite)

        # Physics engine
        # NOTE has to go after everything else is initialised
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player.sprite, self.scene.get_sprite_list("Beats"))

        self.beat_manager = BeatManager()

    def on_draw(self):
        """
        Render the screen.
        """
        # Clears the previous frame
        self.clear()

        # Call draw() on all your sprite lists below

        # Draws the lanes for the beats to spawn in
        self.beat_manager.draw_lanes()
        self.scene.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.scene.update(["Beats"])
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.sprite.change_y = constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.sprite.change_x = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    game = MyGame(constants.SCREEN_WIDTH,
                  constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
