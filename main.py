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
        grid = Grid(gridSize)
        grid.generateGrid()

    def playerOneTurn(self, grid):
        grid.outputGrid()
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        cell = grid.getCell(row - 1, column - 1)
        cell.changeSymbol("X")

    def playerTwoTurn(self, grid):
        grid.outputGrid()
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        cell = grid.getCell(row - 1, column - 1)
        cell.changeSymbol("O")


game = Match()
