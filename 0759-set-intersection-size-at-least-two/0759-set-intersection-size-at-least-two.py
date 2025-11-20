class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))
        a, b = -1, -1
        res = 0

        for start, end in intervals:
            if start > b:
                res += 2
                a, b = end - 1, end
            elif start > a:
                res += 1
                a, b = b, end
        return res