class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        return min(len(set(candyType)), len(candyType) // 2)
        