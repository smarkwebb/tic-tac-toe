class Grid:
    def __init__(self, gridSize):
        self.__grid = []
        self.__gridSize = gridSize

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

    def getSymbol(self):
        return self.__symbol

    def getAssignedPlayer(self):
        return self.__assignedPlayer


class Match:
    def __init__(self):
        gridSize = int(input("Enter grid size: "))
        self.__grid = Grid(gridSize)
        self.__grid.generateGrid()
        self.__currentPlayer = 1

    def playerOneTurn(self):
        self.__grid.outputGrid()
        print("PLAYER ONE TURN")
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        cell = self.__grid.getCell(row - 1, column - 1)
        cell.changeSymbol("X")
        self.__currentPlayer = 2

    def playerTwoTurn(self):
        self.__grid.outputGrid()
        print("PLAYER TWO TURN")
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        cell = self.__grid.getCell(row - 1, column - 1)
        cell.changeSymbol("O")
        self.__currentPlayer = 1

    def update(self):
        if self.__currentPlayer == 1:
            self.playerOneTurn()
        else:
            self.playerTwoTurn()


game = Match()
running = True
while running:
    game.update()
