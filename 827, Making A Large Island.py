# Reference: https://leetcode.com/problems/making-a-large-island/
# Sequence = 827. Making A Large Island
# Prepared by - Maddy Rai
import time
import itertools
import copy


class Solution:
    def tempIsland(selfs, modgrid):
        lsans = []
        row = len(modgrid)
        col = len(modgrid[0])

        def recisland(m, n):
            if modgrid[m][n]:
                modgrid[m][n] = 0

                counte = countw = countn = counts = 0
                if n < col-1 and modgrid[m][n+1]: counte = recisland(m, n + 1)
                if n > 0     and modgrid[m][n-1]: countw = recisland(m, n-1)
                if m > 0     and modgrid[m-1][n]: countn = recisland(m-1, n)
                if m < row-1 and modgrid[m+1][n]: counts = recisland(m+1, n)

                return 1+counte+countw+countn+counts
            else:
                return 0

        for i, j in itertools.product(range(row), range(col)):
            if modgrid[i][j]:
                lsans = lsans + [recisland(i,j)]

        return max(lsans) if lsans else 0


    def largestIsland(self, grid):
        lsfinal = []
        for i, j in itertools.product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j]:
                lsfinal = lsfinal + [Solution.tempIsland(None, copy.deepcopy(grid))]
            else:
                grid[i][j] = 1
                lsfinal = lsfinal + [Solution.tempIsland(None, copy.deepcopy(grid))]
                grid[i][j] = 0


        return max(lsfinal) if lsfinal else 0


grid = [[1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,1],[0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1],[0,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1],[1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1],[1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1],[0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,1],[0,1,0,0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0],[0,1,1,0,0,0,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0],[1,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0],[1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0],[1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0],[0,1,0,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0],[0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,1,1,1,0,1],[0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0],[0,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0],[0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0],[1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0],[1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1],[0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0],[0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0],[0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1],[0,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,1],[0,1,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,1,0],[0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,1,0],[0,1,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0],[0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1],[0,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0],[0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1],[0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,1],[1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1],[0,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,1],[0,1,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1],[1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1],[0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1],[0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0],[0,1,0,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1],[0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0],[1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0],[1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1],[1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,0],[0,1,1,1,1,0,0,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0],[0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1],[1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1],[0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,1],[1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0],[1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,1],[1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,0,0]]

tic = time.perf_counter()
result = Solution.largestIsland(None, grid)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.largestIsland(None, [[1, 0], [0, 1]]) == 3 else print('Failed!!')
print('Pass') if Solution.largestIsland(None, [[1, 1], [1, 1]]) == 4 else print('Failed!!')
print('Pass') if Solution.largestIsland(None, [[1,1],[1,0]]) == 4 else print('Failed!!')
print('Pass') if Solution.largestIsland(None, [[0,1,1],[1,0,0]]) == 4 else print('Failed!!')
print('Pass') if Solution.largestIsland(None, [[]]) == 0 else print('Failed!!')
print('Pass') if Solution.largestIsland(None, [[0]]) == 1 else print('Failed!!')
print('Pass') if Solution.largestIsland(None, [[0,0],[0,0]]) == 1 else print('Failed!!')
print('Pass') if Solution.largestIsland(None, [[1]]) == 1 else print('Failed!!')
print('Pass') if Solution.largestIsland(None, [[1,0],[1,1]]) == 4 else print('Failed!!')