class GameController:
    """ Maintains the state of the game."""
    def __init__(self, BOARD_LENGTH):
        self.BOARD_LENGTH = BOARD_LENGTH
        self.game_end = False
        self.record = False
        self.white_num = 0
        self.black_num = 0

    def display(self):
        """ displays thinking... on the board while waiting for
        the computer making its move"""
        if not self.game_end:
            fill(105, 105, 105)
            textSize(50)
            text("thinking...", self.BOARD_LENGTH/2 - 100, self.BOARD_LENGTH/2)

    def update(self):
        """Carries out necessary actions
        if the white or black wins or they tie"""
        if self.game_end:
            fill(204, 102, 0)
            textSize(35)
            text("WHITE * "+str(self.white_num), self.BOARD_LENGTH/2 - 140,
                 self.BOARD_LENGTH/7*2)
            text("BLACK * "+str(self.black_num), self.BOARD_LENGTH/2 - 140,
                 self.BOARD_LENGTH/7*3)
            if self.white_num > self.black_num:
                textSize(50)
                text("WHITE WINS", self.BOARD_LENGTH/2 - 140,
                     self.BOARD_LENGTH/3*2)
            elif self.white_num < self.black_num:
                textSize(50)
                text("BLACK WINS", self.BOARD_LENGTH/2 - 140,
                     self.BOARD_LENGTH/3*2)
            else:
                textSize(50)
                text("TIE", self.BOARD_LENGTH/2 - 140, self.BOARD_LENGTH/3*2)
            self.record = True

    def record_scores(self):
        """ prompt the user for their name
        save their name and scores in the socres.txt"""
        if self.record:
            with open("scores.txt", "r+") as f:
                name = self.input("enter your name")
                value = name + " " + str(self.black_num) + '\n'
                firstline = f.readline()
                if firstline:
                    space_index = firstline.rfind(" ")
                    max_score = int(firstline[space_index+1:-1])
                    if self.black_num > max_score:
                        lines = [value, firstline]
                        for line in f:
                            lines.append(line)
                        with open("scores.txt", "w") as f2:
                            for line in lines:
                                f2.write(line)
                    else:
                        f.write(value)
                else:
                    f.write(value)
                exit()

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
