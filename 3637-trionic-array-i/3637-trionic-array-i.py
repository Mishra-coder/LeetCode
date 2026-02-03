class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        i = 1

        while i < n and nums[i] > nums[i-1]:
            i += 1
        if i == 1:
            return False

        p = i

        while i < n and nums[i] < nums[i-1]:
            i += 1
        if i == p:
            return False

        q = i

        while i < n and nums[i] > nums[i-1]:
            i += 1
        if i == q:
            return False

        return i == n
