from tiles import Tiles
from gamemanager import GameManager
from game_controller import GameController


class Board:
    """Draws the green board and the disks"""

    def __init__(self, BOARD_LENGTH, SQUARE_LENGTH, DIAMETER, game_controller):
        self.BOARD_LENGTH = BOARD_LENGTH
        self.SQUARE_LENGTH = SQUARE_LENGTH
        self.DIAM = DIAMETER
        self.gc = game_controller
        self.tiles = Tiles(BOARD_LENGTH, SQUARE_LENGTH, DIAMETER)
        self.gm = GameManager(self.tiles)

    def update(self):
        """Make necessary per-frame updates"""
        if (self.tiles.no_blank()) or (
          not self.gm.check_player()) or (
          not self.gm.check_computer()):
            self.gc.game_end = True
            self.gc.black_num = self.tiles.black_num
            self.gc.white_num = self.tiles.white_num

    def display(self):
        """Display the board"""
        self.update()

        # Display the tiles
        self.tiles.display()

        # Draw the disks
        stroke(0.0, 0.0, 0.0)
        strokeWeight(3)
        for i in range(1, self.BOARD_LENGTH//self.SQUARE_LENGTH):
            line(self.SQUARE_LENGTH*i,
                 0,
                 self.SQUARE_LENGTH*i,
                 self.BOARD_LENGTH)
            line(0, self.SQUARE_LENGTH*i,
                 self.BOARD_LENGTH, self.SQUARE_LENGTH*i)
