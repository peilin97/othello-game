from board import Board
from tiles import Tiles
from gamemanager import GameManager
from game_controller import GameController


def test_constructor():
    g = GameController(800)
    b = Board(800, 100, 90, g)
    assert b.BOARD_LENGTH == 800
    assert b.SQUARE_LENGTH == 100
    assert b.DIAM == 90
    assert b.gc is g
    assert b.tiles.black_num == 2
    assert b.tiles.white_num == 2
    assert b.gm.num_of_tiles == 4
