from gamemanager import GameManager
from tiles import Tiles
import copy


def test_constructor():
    t = Tiles(800, 100, 90)
    gm = GameManager(t)
    assert gm.AROUND == [(0, -1), (0, 1), (1, 0), (-1, 0),
                         (1, 1), (-1, -1), (1, -1), (-1, 1)]
    assert gm.player_turn is True
    assert gm.tiles.SQUARES_NUM == 8
    assert gm.tiles.white_num == 2
    assert gm.NUM_OF_TOTAL_SQUARES == 64
    assert gm.CORNERS == [(0, 0), (0, 7), (7, 0), (7, 7)]
    assert gm.num_of_tiles == 4


def test_check_player():
    t = Tiles(800, 100, 90)
    gm = GameManager(t)
    assert gm.check_player() is True


def test_check_computer():
    t = Tiles(800, 100, 90)
    gm = GameManager(t)
    assert gm.check_computer() is True


def test_player_make_move():
    t = Tiles(800, 100, 90)
    gm = GameManager(t)
    # when the player makes an illegal move
    gm.player_make_move(1, 1)
    assert gm.num_of_tiles == 4
    assert gm.tiles.white_num == 2
    # when the player makes a legal move
    gm.player_make_move(250, 350)
    assert gm.num_of_tiles == 5
    assert gm.tiles.white_num == 1


def test_computer_make_move():
    t = Tiles(800, 100, 90)
    gm = GameManager(t)
    gm.player_make_move(250, 350)
    gm.computer_make_move()
    assert gm.num_of_tiles == 6
    assert gm.player_turn is True
    assert gm.tiles.white_num == 3


def test_iscorner():
    t = Tiles(800, 100, 90)
    gm = GameManager(t)
    assert gm.iscorner(0, 0) is True
    assert gm.iscorner(1, 1) is False


def test_forecast():
    t = Tiles(800, 100, 90)
    gm = GameManager(t)
    gm.player_make_move(250, 350)
    gm.computer_make_move()
    gm.player_make_move(350, 250)
    mock_squares = copy.deepcopy(gm.tiles.squares)
    mock_player_tiles = copy.deepcopy(gm.tiles.player_tiles)
    mock_computer_tiles = copy.deepcopy(gm.tiles.computer_tiles)
    assert gm.forecast(mock_squares, mock_player_tiles,
                       mock_computer_tiles,
                       [(3, 2), (4, 3)],
                       4, 2) == 9


def test_islegal():
    t = Tiles(800, 100, 90)
    gm = GameManager(t)
    assert gm.islegal(gm.tiles.player_tiles, gm.tiles.computer_tiles,
                      0, 0) == []
    assert gm.islegal(gm.tiles.player_tiles, gm.tiles.computer_tiles,
                      3, 2) == [(3, 3)]
