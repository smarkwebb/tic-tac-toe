class Grid:
    def __init__(self, gridSize):
        self.__grid = []
        self.__gridSize = gridSize

    def generateGrid(self):
        for row in range(0, self.__gridSize):
            self.__grid.append([])
            for column in range(0, self.__gridSize):
                self.__grid[row].append("-")

    def outputGrid(self):
        for row in range(0, self.__gridSize):
            for column in range(0, self.__gridSize):
                print(self.__grid[row][column], end="")
            print("")
