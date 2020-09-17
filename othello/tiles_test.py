from tiles import Tiles


def test_constructor():
    t = Tiles(800, 100, 90)
    assert t.BOARD_LENGTH == 800
    assert t.SQUARE_LENGTH == 100
    assert t.SQUARES_NUM == 8
    assert t.DIAM == 90
    assert t.black_num == 2
    assert t.white_num == 2
    assert t.squares[0][0].x == 50
    assert t.squares[1][1].x == 150
    assert t.player_tiles[0][0] == 0
    assert t.player_tiles[3][4].x == 450
    assert t.player_tiles[3][4].y == 350
    assert t.player_tiles[4][3].x == 350
    assert t.player_tiles[4][3].y == 450
    assert t.computer_tiles[3][3].x == 350
    assert t.computer_tiles[3][3].y == 350
    assert t.computer_tiles[4][4].x == 450
    assert t.computer_tiles[4][4].y == 450


def test_add_black():
    t = Tiles(800, 100, 90)
    t.add_black(0, 0)
    assert t.black_num == 3
    assert t.squares[0][0] == 0
    assert t.player_tiles[0][0].x == 50
    assert t.player_tiles[0][0].y == 50


def test_add_white():
    t = Tiles(800, 100, 90)
    t.add_white(0, 0)
    assert t.white_num == 3
    assert t.squares[0][0] == 0
    assert t.computer_tiles[0][0].x == 50
    assert t.computer_tiles[0][0].y == 50


def test_black_to_white():
    t = Tiles(800, 100, 90)
    t.black_to_white([(3, 4), (4, 3)])
    assert t.white_num == 4
    assert t.black_num == 0


def test_white_to_black():
    t = Tiles(800, 100, 90)
    t.white_to_black([(3, 3), (4, 4)])
    assert t.white_num == 0
    assert t.black_num == 4


def test_no_blank():
    t = Tiles(800, 100, 90)
    assert t.no_blank() is False
    t.squares = [[0]*8 for i in range(8)]
    assert t.no_blank() is True


def test_len_to_index():
    t = Tiles(800, 100, 90)
    assert t.len_to_index(50) == 0
    assert t.len_to_index(750) == 7


def test_index_to_len():
    t = Tiles(800, 100, 90)
    assert t.index_to_len(0) == 50
    assert t.index_to_len(7) == 750
