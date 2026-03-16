class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        
        n = len(s)
        res = [n] * n
        prev = -n
        
        for i in range(n):
            if s[i] == c:
                prev = i
            res[i] = i - prev
        
        prev = 2 * n
        
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i)
        
        return res