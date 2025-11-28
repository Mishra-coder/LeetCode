from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ans = [0]  

        def dfs(u, parent):
            s = values[u]

            for v in g[u]:
                if v != parent:
                    s += dfs(v, u)

            if s % k == 0:
                ans[0] += 1
                return 0

            return s

        dfs(0, -1)
        return ans[0]
