class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        even = 0
        odd = 0

        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)
        