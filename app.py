from ComputerClass import Computer
from game import displayBoard, GameOver, intro, checkGame, displayBoard, playerStep

boardGame = [];
player = "x"
comp = "o"

intro(boardGame, player, comp)
cpm = Computer(comp)

while(not GameOver(boardGame)):
    if player == 'x':
        displayBoard(boardGame)
        playerStep(boardGame, player)
        checkGame(boardGame)
        cpm.step(boardGame)
        checkGame(boardGame)
    else:
        cpm.step(boardGame)
        checkGame(boardGame)
        playerStep(boardGame, player)
        checkGame(boardGame)
