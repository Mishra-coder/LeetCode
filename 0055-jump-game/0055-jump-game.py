class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        far = 0
        
        for i in range(len(nums)):
            if i > far:
                return False
            far = max(far, i + nums[i])
        
        return True