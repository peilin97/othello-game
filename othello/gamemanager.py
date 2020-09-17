import copy
from tile import Tile


class GameManager():
    """Handels the turn taking between the player and the computer
       checks legal moves and find the optimal move for the computer"""

    def __init__(self, tiles):
        self.AROUND = [(0, -1), (0, 1), (1, 0), (-1, 0),
                       (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.player_turn = True
        self.tiles = tiles
        self.NUM_OF_TOTAL_SQUARES = (self.tiles.SQUARES_NUM) ** 2
        self.CORNERS = [(0, 0),
                        (0, self.tiles.SQUARES_NUM - 1),
                        (self.tiles.SQUARES_NUM - 1, 0),
                        (self.tiles.SQUARES_NUM - 1,
                         self.tiles.SQUARES_NUM - 1)]
        self.num_of_tiles = 4

    def check_player(self):
        """ check whether the player has possible legal moves """
        for row in range(self.tiles.SQUARES_NUM):
            for col in range(self.tiles.SQUARES_NUM):
                if self.tiles.squares[row][col]:
                    flipped_loc = self.islegal(self.tiles.player_tiles,
                                               self.tiles.computer_tiles,
                                               row, col)
                    if flipped_loc:  # player has legal moves
                        return True
        # no legal moves for the player
        # check computer
        for row in range(self.tiles.SQUARES_NUM):
            for col in range(self.tiles.SQUARES_NUM):
                if self.tiles.squares[row][col]:
                    flipped_loc = self.islegal(self.tiles.computer_tiles,
                                               self.tiles.player_tiles,
                                               row, col)
                    if flipped_loc:
                        self.player_turn = False
                        return True
        # no legal moves for computer or player
        return False

    def check_computer(self):
        for row in range(self.tiles.SQUARES_NUM):
            for col in range(self.tiles.SQUARES_NUM):
                if self.tiles.squares[row][col]:
                    flipped_loc = self.islegal(self.tiles.computer_tiles,
                                               self.tiles.player_tiles,
                                               row, col)
                    if flipped_loc:  # computer has legal moves
                        return True
        # no legal moves for computer
        # check player
        for row in range(self.tiles.SQUARES_NUM):
            for col in range(self.tiles.SQUARES_NUM):
                if self.tiles.squares[row][col]:
                    flipped_loc = self.islegal(self.tiles.player_tiles,
                                               self.tiles.computer_tiles,
                                               row, col)
                    if flipped_loc:  # player has legal moves
                        self.player_turn = True
                        return True
        # no legal moves for computer or player
        return False

    def player_make_move(self, mouseX, mouseY):
        """ update the player's move """
        if self.player_turn:
            # check whether the clicked square is blank
            if (mouseX not in list(range(0, self.tiles.BOARD_LENGTH,
                self.tiles.SQUARE_LENGTH))) and (
                 mouseY not in list(range(0, self.tiles.BOARD_LENGTH,
                                    self.tiles.SQUARE_LENGTH))):
                # not click on the line
                row = mouseY // self.tiles.SQUARE_LENGTH
                col = mouseX // self.tiles.SQUARE_LENGTH
                if self.tiles.squares[row][col]:
                    # check whether the blank square is legal
                    white_loc = self.islegal(self.tiles.player_tiles,
                                             self.tiles.computer_tiles,
                                             row, col)
                    if white_loc:  # if the square is legal
                        self.tiles.white_to_black(white_loc)  # flip
                        self.tiles.add_black(row, col)
                        self.player_turn = False
                        self.num_of_tiles += 1
                        result = self.check_computer()
                        if result and (not self.player_turn):
                            print("computer's turn...")
                        elif result and self.player_turn:
                            print("no legal moves for the computer,",
                                  "swicth to the player")
                            print("player's turn...")

    def computer_make_move(self):
        """ checks whether the computer has the legal move
        computer chooses the best move """
        if not self.player_turn:
            # computer has legal moves
            if self.check_computer() and (not self.player_turn):
                # find the best location
                done = False
                opti_location = ()
                optimal_flipped = []
                black_num = 0
                white_num = 0
                squares_num = 0
                mock_player_tiles = copy.deepcopy(self.tiles.player_tiles)
                mock_computer_tiles = copy.deepcopy(self.tiles.computer_tiles)
                mock_squares = copy.deepcopy(self.tiles.squares)

                for row in range(self.tiles.SQUARES_NUM):
                    for col in range(self.tiles.SQUARES_NUM):
                        if self.tiles.squares[row][col]:
                            flipped = self.islegal(self.tiles.computer_tiles,
                                                   self.tiles.player_tiles,
                                                   row, col)
                            # corners are the first choice to be considered
                            if len(flipped) > 0 and self.iscorner(row, col):
                                optimal_flipped = copy.deepcopy(flipped)
                                opti_location = (row, col)
                                done = True
                                break
                            # when the game has
                            # less than quarter of the discs being placed
                            # flipping less of opponent tiles is better
                            elif self.num_of_tiles < (
                                 self.NUM_OF_TOTAL_SQUARES//4):
                                if len(flipped) > 0 and (
                                     len(optimal_flipped) == 0):
                                    optimal_flipped = copy.deepcopy(flipped)
                                    opti_location = (row, col)
                                elif (len(flipped) > 0) and (len(
                                       optimal_flipped) > len(flipped)):
                                    optimal_flipped = copy.deepcopy(flipped)
                                    opti_location = (row, col)
                            else:
                                # when the game has
                                # more than a quarter of the discs being placed
                                # flipping more of opponent tiles is better
                                if len(flipped) > len(optimal_flipped):
                                    optimal_flipped = copy.deepcopy(flipped)
                                    opti_location = (row, col)
                                elif (len(optimal_flipped) != 0) and (
                                      len(flipped) == len(optimal_flipped)):
                                    # when another square can flip black tiles
                                    # as same as the current optimal square
                                    # check which square is better
                                    # the better one is the square which makes
                                    # the player has less
                                    # number of move options
                                    forecast_flip = self.forecast(
                                        mock_squares,
                                        mock_player_tiles,
                                        mock_computer_tiles, flipped, row, col)
                                    forecast_optimal_flipped = self.forecast(
                                        mock_squares, mock_player_tiles,
                                        mock_computer_tiles, optimal_flipped,
                                        opti_location[0], opti_location[1])
                                    if forecast_flip < (
                                     forecast_optimal_flipped):
                                        optimal_flipped = copy.deepcopy(
                                            flipped)
                                        opti_location = (row, col)
                    if done:
                        break
                self.tiles.black_to_white(optimal_flipped)
                self.tiles.add_white(opti_location[0], opti_location[1])
                self.num_of_tiles += 1
                self.player_turn = True
                result = self.check_player()
                if result and (self.player_turn):
                    print("player's turn...")
                elif result and (not self.player_turn):
                    print("no legal moves for the player,",
                          "swicth to the computer")
                    print("computer's turn...")

    def iscorner(self, row, col):
        """Check whether the location is in corcer"""
        if (row, col) in self.CORNERS:
            return True
        return False

    def forecast(self, mock_squares, mock_player_tiles, mock_computer_tiles,
                 locations, row, col):
        """forecast the number of the player's next move options"""
        # flip black tiles to white tiles
        for location in locations:
            r, c = location[0], location[1]
            mock_player_tiles[r][c] = 0
            mock_computer_tiles[r][c] = Tile(self.tiles.index_to_len(c),
                                             self.tiles.index_to_len(r),
                                             self.tiles.DIAM)
        # put the white tile to the square
        mock_squares[row][col] = 0
        mock_computer_tiles[row][col] = Tile(self.tiles.index_to_len(col),
                                             self.tiles.index_to_len(row),
                                             self.tiles.DIAM)
        # forecast the player's move
        player_options = 0
        for row in range(self.tiles.SQUARES_NUM):
            for col in range(self.tiles.SQUARES_NUM):
                if mock_squares[row][col]:
                    forecast_flip = self.islegal(mock_player_tiles,
                                                 mock_computer_tiles,
                                                 row, col)
                    if len(forecast_flip) > 0:
                        player_options += 1
        return player_options

    def islegal(self, current_tiles, opponent_tiles, row, col):
        """Given the clicked square's row and column number
        check whether the clicked blank square is legal
        if it is true, records positions of opponent tiles
        which will be flipped"""
        count = []
        for (r, c) in self.AROUND:
            side_count = []
            n_row = row + r
            n_col = col + c

            while (n_row >= 0) and (n_row < self.tiles.SQUARES_NUM) and (
                   n_col >= 0) and (n_col < self.tiles.SQUARES_NUM):
                if opponent_tiles[n_row][n_col]:
                    side_count.append((n_row, n_col))
                    n_row += r
                    n_col += c
                elif side_count and current_tiles[n_row][n_col]:
                    count += side_count
                    break
                else:
                    break
        return count
