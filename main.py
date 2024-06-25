class Grid:
    def __init__(self, gridSize):
        self.__grid = []
        self.__gridSize = gridSize

    def generateGrid(self):
        for row in range(0, self.__gridSize):
            self.__grid.append([])
            for column in range(0, self.__gridSize):
                symbol = Symbol("-", None)
                self.__grid[row].append(symbol)

    def outputGrid(self):
        for row in range(0, self.__gridSize):
            for column in range(0, self.__gridSize):
                print(self.__grid[row][column].getSymbol(), end="")
            print("")


class Symbol:
    def __init__(self, symbol, assignedPlayer):
        self.__symbol = symbol
        self.__assignedPlayer = assignedPlayer

    def getSymbol(self):
        return self.__symbol

    def getAssignedPlayer(self):
        return self.__assignedPlayer
