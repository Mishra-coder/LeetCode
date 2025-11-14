class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = 10**15
        dist = [INF] * n
        dist[src] = 0
        
        for _ in range(k + 1):
            temp = dist[:]
            for u, v, w in flights:
                if dist[u] + w < temp[v]:
                    temp[v] = dist[u] + w
            dist = temp
        
        return -1 if dist[dst] == INF else dist[dst]
