import random


class Grid:
    def __init__(self, gridSize):
        self.__grid = []
        self.__gridSize = gridSize

    def checkWin(self):
        for row in range(0, self.__gridSize):
            for column in range(0, self.__gridSize):
                if self.__grid[row][column].getSymbol() != "-":
                    try:
                        if self.__grid[row][column].getSymbol() == self.__grid[row][column + 1].getSymbol() == self.__grid[row][column + 2].getSymbol():
                            return self.__grid[row][column].getAssignedPlayer()
                        if self.__grid[row][column].getSymbol() == self.__grid[row + 1][column].getSymbol() == self.__grid[row + 2][column].getSymbol():
                            return self.__grid[row][column].getAssignedPlayer()
                    except:
                        pass

    def generateGrid(self):
        for row in range(0, self.__gridSize):
            self.__grid.append([])
            for column in range(0, self.__gridSize):
                symbol = Cell("-", None)
                self.__grid[row].append(symbol)

    def outputGrid(self):
        for row in range(0, self.__gridSize):
            for column in range(0, self.__gridSize):
                print(self.__grid[row][column].getSymbol(), end="")
            print("")

    def getGrid(self):
        return self.__grid

    def getCell(self, row, column):
        return self.__grid[row][column]


class Cell:
    def __init__(self, symbol, assignedPlayer):
        self.__symbol = symbol
        self.__assignedPlayer = assignedPlayer

    def changeSymbol(self, newSymbol):
        self.__symbol = newSymbol

    def changeAssignedPlayer(self, newAssignedPlayer):
        self.__assignedPlayer = newAssignedPlayer

    def getSymbol(self):
        return self.__symbol

    def getAssignedPlayer(self):
        return self.__assignedPlayer


class Match:
    def __init__(self):
        self.__currentPlayer = 1
        self.configureMatch()

    def configureMatch(self):
        self.__gridSize = int(input("Enter grid size: "))
        self.__grid = Grid(self.__gridSize)
        self.__grid.generateGrid()

    def playerOneTurn(self):
        self.__grid.outputGrid()
        print("PLAYER ONE TURN")
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        cell = self.__grid.getCell(row - 1, column - 1)
        if cell.getAssignedPlayer() == None:
            cell.changeAssignedPlayer(1)
            cell.changeSymbol("X")
            self.__currentPlayer = 2
        else:
            print("You can only select empty cells")

    def playerTwoTurn(self):
        self.__grid.outputGrid()
        print("PLAYER TWO TURN")
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        cell = self.__grid.getCell(row - 1, column - 1)
        if cell.getAssignedPlayer() == None:
            cell.changeAssignedPlayer(2)
            cell.changeSymbol("O")
            self.__currentPlayer = 1
        else:
            print("You can only select empty cells")

    def botTurn(self):
        self.__grid.outputGrid()
        print("BOT TURN")
        row = random.randint(0, self.__gridSize)
        print("Enter row:", row)
        column = random.randint(0, self.__gridSize)
        print("Enter column:", column)
        cell = self.__grid.getCell(row - 1, column - 1)
        if cell.getAssignedPlayer() == None:
            cell.changeAssignedPlayer(2)
            cell.changeSymbol("O")
            self.__currentPlayer = 1
        else:
            print("You can only select empty cells")

    def update(self):
        if self.__currentPlayer == 1:
            self.playerOneTurn()
        else:
            self.playerTwoTurn()
        winner = self.__grid.checkWin()
        return winner


game = Match()
winner = None
while not winner:
    winner = game.update()
print("WINNER: PLAYER", winner)
