import constants
import arcade
from colours import Colours
from beat import Beat
from typing import List

class Conductor:
    def __init__(self):
        self.song = None
        self.song_player = None
        self.song_length = 0
        self.bpm = 0
        self.crotchet = 0
        self.offset = 0
        self.song_position = 0

    def set_song(self, song):
        self.song = song
        self.song_length = song.get_length()

    def set_bpm(self, bpm):
        self.bpm = bpm
        self.crotchet = bpm / 60.0

    def set_offset(self, offset):
        self.offset = offset

    def update_song_position(self):
        self.song_position = self.song.get_stream_position(self.song_player) - self.offset

    def play(self):
        # if not self.song.is_playing(self):
        self.song_player = self.song.play()

    def reset(self):
        self.song_position = 0