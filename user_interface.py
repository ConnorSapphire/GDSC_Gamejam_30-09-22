from asyncio import constants
import time
import arcade
import constants

class UserInterface:
    def __init__(self) -> None:
        pass
        self.tutorial_done = False
        self.starttime = time.time()
        self.message_idx = 0
        self.messages = [
           f"Welcome to the {constants.GAME_NAME}!",
           f"Move with the left and right arrow keys",
           f"Press 'a' for red, 's' for green, 'd' for blue", #WARNING magic values for keys
        ]

    def tutorial(self):

        # Works
        if (self.message_idx >= self.messages.__len__()):
            self.tutorial_done = True
            return
        self.should_display = True
        self.currenttime = time.time()
        self.elapsedtime = self.currenttime - self.starttime
        if (self.elapsedtime >= 5):
            self.starttime = time.time()
            self.should_display = False
            self.message_idx += 1

        if (self.should_display):
            #WARNING magic values for position
            arcade.draw_text(self.messages[self.message_idx], constants.SCREEN_WIDTH / 2 - 150, 300, arcade.color.WHITE, 20, font_name="Kenney Pixel")



        # print(f"start: {self.starttime}. Cur: {self.currenttime}. Elapsed: {self.elapsedtime}")

    # def stopwatch(self, duration: int) -> None:
    #     starttime = time.time()

    #     if (starttime + duration) < time.time():
    #         print("Time left: ", starttime + duration - time.time())
    #         self.should_display = False

