from typing import List
import math

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        ALPHA = 26
        dist = [[math.inf] * ALPHA for _ in range(ALPHA)]
        
        for i in range(ALPHA):
            dist[i][i] = 0
        
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        for k in range(ALPHA):
            for i in range(ALPHA):
                for j in range(ALPHA):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == math.inf:
                return -1
            total += dist[u][v]
        
        return total
