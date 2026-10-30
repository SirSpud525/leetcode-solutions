class Solution:
   def createGrid(self, m: int, n: int) -> list[str]:
       def makelist(m,n,filler):
           a = [filler for x in range(m)]
           b = [[filler] * n for i in range(m)]
           return b
       grid = makelist(m, n, "#")
       for i in range(n):
           grid[0][i] = "."
       for i in range(m):
           grid[i][n-1] = "."
       for i in range(m):
           grid[i] = "".join(grid[i])
       return grid


