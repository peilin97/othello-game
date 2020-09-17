from game_controller import GameController


def test_constructor():
    gc = GameController(800)
    assert gc.BOARD_LENGTH == 800
    assert gc.game_end is False
    assert gc.record is False
    assert gc.white_num == 0
    assert gc.black_num == 0
