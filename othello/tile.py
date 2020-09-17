class Tile:
    """A Tile"""
    def __init__(self, x, y, DIAM):
        self.x = x
        self.y = y
        self.DIAM = DIAM

    def display(self):
        """Draws the tile"""
        ellipse(self.x, self.y, self.DIAM, self.DIAM)
