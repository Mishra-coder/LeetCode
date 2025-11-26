class Solution:
    def numberOfPaths(self, grid, k):
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0]*k for _ in range(n)]
        dp[0][grid[0][0] % k] = 1
        
        for j in range(1, n):
            add = grid[0][j] % k
            nxt = [0]*k
            for r in range(k):
                if dp[j-1][r]:
                    nxt[(r+add)%k] = (nxt[(r+add)%k] + dp[j-1][r]) % mod
            dp[j] = nxt
        
        for i in range(1, m):
            add = grid[i][0] % k
            nxt = [0]*k
            for r in range(k):
                if dp[0][r]:
                    nxt[(r+add)%k] = (nxt[(r+add)%k] + dp[0][r]) % mod
            dp[0] = nxt
            
            for j in range(1, n):
                add = grid[i][j] % k
                nxt = [0]*k
                for r in range(k):
                    if dp[j][r]:
                        nxt[(r+add)%k] = (nxt[(r+add)%k] + dp[j][r]) % mod
                for r in range(k):
                    if dp[j-1][r]:
                        nxt[(r+add)%k] = (nxt[(r+add)%k] + dp[j-1][r]) % mod
                dp[j] = nxt
        
        return dp[-1][0]
