
"""
@from https://api.arcade.academy/en/latest/examples/starting_template.html#starting-template
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import random
import arcade
import game_constants
from beat import Beat
from colours import Colours
from player import Player


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
        
        # Physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player.sprite, self.scene.get_sprite_list("Beats"))

        # Testing area
        self.beat_list = arcade.SpriteList()
        self.test_beat = Beat(Colours.BLUE, 0)
        self.test_beat2 = Beat(Colours.BLUE, 2)
        self.scene.add_sprite("Beats", self.test_beat.sprite)
        self.scene.add_sprite("Beats", self.test_beat2.sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.scene.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.physics_engine.update()

        # TODO
        # Selects a random lane for the beat to spawn in. It continues to move down until reaching a certain x/y,
        # at which point it is removed from the list.


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.sprite.change_y = game_constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.sprite.change_y = -game_constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.sprite.change_x = -game_constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.sprite.change_x = game_constants.PLAYER_MOVEMENT_SPEED

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
    game = MyGame(game_constants.SCREEN_WIDTH,
                  game_constants.SCREEN_HEIGHT, game_constants.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
