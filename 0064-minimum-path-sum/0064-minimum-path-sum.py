class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        memo = {}
        def solve(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float("inf")
            if (i,j) in memo:
                return memo[(i,j)]
            else:
                memo[(i,j)] = grid[i][j] + min(solve(i-1, j), solve(i, j-1))
            return memo[(i,j)]
        return solve(m-1, n-1)
            