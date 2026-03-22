from collections import Counter
import math
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        freq = {}
        for num in deck:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = 0
        for v in freq.values():
            g = gcd(g, v)

        return g >= 2
        