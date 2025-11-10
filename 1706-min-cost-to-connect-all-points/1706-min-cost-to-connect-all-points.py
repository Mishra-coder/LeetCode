class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        import heapq
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]
        total_cost = 0
        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            total_cost += cost
            visited.add(i)
            for j in range(n):
                if j not in visited:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    new_cost = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (new_cost, j))
        return total_cost

