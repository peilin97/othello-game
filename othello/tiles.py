from tile import Tile
import copy


class Tiles():
    """Controls the computer's and the player's tiles and empty squares"""

    def __init__(self, BOARD_LENGTH, SQUARE_LENGTH, DIAM):
        self.BOARD_LENGTH = BOARD_LENGTH
        self.SQUARE_LENGTH = SQUARE_LENGTH
        self.SQUARES_NUM = self.BOARD_LENGTH//self.SQUARE_LENGTH
        self.DIAM = DIAM
        self.black_num = 2
        self.white_num = 2

        #  initialize all squares with 0
        self.squares = [[0]*self.SQUARES_NUM for i in range(
            self.SQUARES_NUM)]
        self.player_tiles = copy.deepcopy(self.squares)
        self.computer_tiles = copy.deepcopy(self.squares)
        for x in range(int(self.SQUARE_LENGTH/2), self.BOARD_LENGTH,
                       self.SQUARE_LENGTH):
            for y in range(int(self.SQUARE_LENGTH/2), self.BOARD_LENGTH,
                           self.SQUARE_LENGTH):
                if (x == self.BOARD_LENGTH/2-self.SQUARE_LENGTH/2) and (
                 y == self.BOARD_LENGTH/2-self.SQUARE_LENGTH/2):
                    self.computer_tiles[self.SQUARES_NUM//2-1][
                        self.SQUARES_NUM//2-1] = Tile(x, y, self.DIAM)
                elif (x == self.BOARD_LENGTH/2-self.SQUARE_LENGTH/2) and (
                   y == self.BOARD_LENGTH/2+self.SQUARE_LENGTH/2):
                    self.player_tiles[self.SQUARES_NUM//2][
                        self.SQUARES_NUM//2-1] = Tile(x, y, self.DIAM)
                elif (x == self.BOARD_LENGTH/2+self.SQUARE_LENGTH/2) and (
                   y == self.BOARD_LENGTH/2-self.SQUARE_LENGTH/2):
                    self.player_tiles[self.SQUARES_NUM//2-1][
                        self.SQUARES_NUM//2] = Tile(x, y, self.DIAM)
                elif (x == self.BOARD_LENGTH/2+self.SQUARE_LENGTH/2) and (
                   y == self.BOARD_LENGTH/2+self.SQUARE_LENGTH/2):
                    self.computer_tiles[self.SQUARES_NUM//2][
                        self.SQUARES_NUM//2] = Tile(x, y, self.DIAM)
                else:
                    self.squares[self.len_to_index(y)][
                        self.len_to_index(x)] = Tile(x, y, self.DIAM)

    def display(self):
        """ Draws the white and black tiles in the board"""
        for row in self.computer_tiles:
            for computer_tile in row:
                if computer_tile:  # if it is not 0
                    fill(255, 255, 255)  # white
                    computer_tile.display()

        for row in self.player_tiles:
            for player_tile in row:
                if player_tile:  # if it is not 0
                    fill(0, 0, 0)  # black
                    player_tile.display()

    def add_black(self, row, col):
        """ given the blank square's position, add it to the player's tiles"""
        self.squares[row][col] = 0
        self.player_tiles[row][col] = Tile(self.index_to_len(col),
                                           self.index_to_len(row),
                                           self.DIAM)
        self.black_num += 1

    def add_white(self, row, col):
        """
        given the blank square's position, add it to the computer's tiles
        """
        self.squares[row][col] = 0
        self.computer_tiles[row][col] = Tile(self.index_to_len(col),
                                             self.index_to_len(row),
                                             self.DIAM)
        self.white_num += 1

    def black_to_white(self, locations):
        """given a list of black tiles' locations, flip them to white tiles"""
        for location in locations:
            row, col = location[0], location[1]
            self.player_tiles[row][col] = 0
            self.computer_tiles[row][col] = Tile(self.index_to_len(col),
                                                 self.index_to_len(row),
                                                 self.DIAM)
        self.white_num += len(locations)
        self.black_num -= len(locations)

    def white_to_black(self, locations):
        """given a list of white tiles' locations, flip them to black tiles"""
        for location in locations:
            row, col = location[0], location[1]
            self.computer_tiles[row][col] = 0
            self.player_tiles[row][col] = Tile(self.index_to_len(col),
                                               self.index_to_len(row),
                                               self.DIAM)
        self.white_num -= len(locations)
        self.black_num += len(locations)

    def no_blank(self):
        """returns True when no blank squares exist"""
        for row in self.squares:
            for square in row:
                if square:
                    return False
        return True

    def len_to_index(self, len):
        """Convert the coordinate number to the index number"""
        return (len-self.SQUARE_LENGTH//2)//self.SQUARE_LENGTH

    def index_to_len(self, i):
        """Convert the index to the coordinate number """
        return i*self.SQUARE_LENGTH + self.SQUARE_LENGTH//2
