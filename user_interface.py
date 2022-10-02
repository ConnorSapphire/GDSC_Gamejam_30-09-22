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
           f"Welcome to {constants.GAME_NAME}! Here's how to play:",
           f"Move with the {constants.KEY_LEFT} and {constants.KEY_RIGHT} keys to get in the same lane as a note",
           f"Press {constants.KEY_BLUE} for blue, {constants.KEY_RED} for red, {constants.KEY_YELLOW} for yellow",
           f"Hit the notes when their centre lines up for a perfect hit!",
           f"Press buttons at the same time to hit new coloured beats. See the colour wheel for more info!",
           "Good luck!"
        ]

    def tutorial(self):

        # Works
        if (self.message_idx >= self.messages.__len__()):
            self.tutorial_done = True
            return
        self.should_display = True
        self.currenttime = time.time()
        self.elapsedtime = self.currenttime - self.starttime
        if (self.elapsedtime >= constants.MSG_DISPLAY_TIME):
            self.starttime = time.time()
            self.should_display = False
            self.message_idx += 1

        if (self.should_display):
            #WARNING magic values for position
            arcade.draw_text(self.messages[self.message_idx], constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, arcade.color.WHITE, 20, font_name="Kenney Pixel", anchor_x="center", anchor_y="center")



        # print(f"start: {self.starttime}. Cur: {self.currenttime}. Elapsed: {self.elapsedtime}")

    # def stopwatch(self, duration: int) -> None:
    #     starttime = time.time()

    #     if (starttime + duration) < time.time():
    #         print("Time left: ", starttime + duration - time.time())
    #         self.should_display = False

