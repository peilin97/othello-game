from board import Board
from game_controller import GameController

BOARD_LENGTH = 800
SQUARE_LENGTH = 100
DIAM = 90
WAIT_TIME = 75
counter = 0
game_controller = GameController(BOARD_LENGTH)
board = Board(BOARD_LENGTH, SQUARE_LENGTH, DIAM, game_controller)

              
def setup():
    size(BOARD_LENGTH, BOARD_LENGTH)
    # background(1, 106, 32)
    
def draw():
    global counter
    background(1, 106, 32)
    board.display()
    game_controller.record_scores()
    game_controller.update()
    if (not board.gm.player_turn) and (counter < WAIT_TIME):
        counter += 1
        game_controller.display()
    elif (not board.gm.player_turn) and (counter == WAIT_TIME):
        board.gm.computer_make_move()
        counter = 0
        
    
def mousePressed():
    board.gm.player_make_move(mouseX, mouseY)
