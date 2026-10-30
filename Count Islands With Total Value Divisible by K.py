class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        islandsCounter = grid.copy()
        # print(islandsCounter)
        islands = []

        def checkCells(x, y):
            toAdd = 0
            try:
                if islandsCounter[x + 1][y] != 0:
                    toAdd += islandsCounter[x + 1][y]
                    islandsCounter[x + 1][y] = 0
                    toAdd += checkCells(x + 1, y)
            except:
                pass
            try:
                if x - 1 >= 0:
                    if islandsCounter[x - 1][y] != 0:
                        toAdd += islandsCounter[x - 1][y]
                        islandsCounter[x - 1][y] = 0
                        toAdd += checkCells(x - 1, y)
            except:
                pass
            try:
                if islandsCounter[x][y + 1] != 0:
                    toAdd += islandsCounter[x][y + 1]
                    islandsCounter[x][y + 1] = 0
                    toAdd += checkCells(x, y + 1)
            except:
                pass
            try:
                if y - 1 >= 0:
                    if islandsCounter[x][y - 1] != 0:
                        toAdd += islandsCounter[x][y - 1]
                        islandsCounter[x][y - 1] = 0
                        toAdd += checkCells(x, y - 1)
            except:
                pass
            # print(toAdd)
            # print(islandsCounter)
            return toAdd

        for i in range(len(islandsCounter)):
            for j in range(len(islandsCounter[i])):
                if (islandsCounter[i][j] == 0):
                    continue
                to = islandsCounter[i][j]
                islandsCounter[i][j] = 0
                islands.append(checkCells(i, j) + to)
                # print(islands)
        toReturn = 0
        for island in islands:
            if island % k == 0:
                toReturn += 1
        return toReturn




