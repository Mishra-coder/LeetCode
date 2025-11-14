class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = [i for i in range(numCourses) if indegree[i] == 0]
        order = []
        idx = 0
        
        while idx < len(q):
            u = q[idx]
            idx += 1
            order.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        return order if len(order) == numCourses else []
