class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        batteries.sort()
        left, right = 0, sum(batteries) // n

        def can_run(T):
            total = 0
            for b in batteries:
                total += min(b, T)
            return total >= n * T

        while left < right:
            mid = (left + right + 1) // 2
            if can_run(mid):
                left = mid
            else:
                right = mid - 1

        return left
        