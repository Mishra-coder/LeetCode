class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        def bfs(r, c):
            q = [(r, c)]       
            grid[r][c] = "0"    
            while q:
                x, y = q.pop(0)   


                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        q.append((nx, ny))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    ans += 1
                    bfs(i, j)

        return ans
