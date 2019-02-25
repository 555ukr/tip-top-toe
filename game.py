def displayBoard(boardGame):
    print("BoardGame")
    for index, value in enumerate(boardGame):
        if (index % 3 == 0 and index != 0):
            print("")
        print(" %s " % value, end="")
    print("")

def GameOver(board):
    end = True;

    for i in board:
        if isinstance(i, int):
            end = False
        # print(type(i))
    # print(end)
    return end;

def intro(boardGame, player, comp):
    for i in range(9):
        boardGame.append(i)
    print(" Game is started ")
    res = input(" Are you going to be first (y/n)?\n ")
    if res == "n":
        player = "0"
        comp = "x"

def playerStep(boardGame, player):
    res = input(" You are next(choose number from 0 to 9):")
    boardGame[int(res)] = player

def checkGame(boardGame):
    
