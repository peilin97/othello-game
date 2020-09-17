from tile import Tile


def test_constructor():
    t = Tile(50, 50, 90)
    assert t.x == 50
    assert t.y == 50
    assert t.DIAM == 90
