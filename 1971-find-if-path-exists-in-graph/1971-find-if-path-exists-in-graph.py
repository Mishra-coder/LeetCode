class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        from collections import deque
        q = deque([source])
        visited = [False] * n
        visited[source] = True
        
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)
        
        return False
        