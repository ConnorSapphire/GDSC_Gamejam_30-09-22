import arcade

# Initialise final static variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOUR = arcade.csscolor.LIGHT_GRAY
GAME_NAME = "GAME JAM GAME"

class MyGame(arcade.Window):
    '''Main application class'''

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME)

        arcade.set_background_color(BACKGROUND_COLOUR)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here



def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
