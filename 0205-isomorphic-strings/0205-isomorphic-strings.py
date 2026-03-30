class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapST = {}
        mapTS = {}
        
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            
            if c1 in mapST:
                if mapST[c1] != c2:
                    return False
            else:
                mapST[c1] = c2
            
            if c2 in mapTS:
                if mapTS[c2] != c1:
                    return False
            else:
                mapTS[c2] = c1
        
        return True
        