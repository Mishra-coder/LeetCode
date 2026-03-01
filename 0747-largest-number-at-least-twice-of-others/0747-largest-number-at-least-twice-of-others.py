class Solution(object):
    def dominantIndex(self, nums):
        max1 = -1
        max2 = -1
        index = -1
        
        for i in range(len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
                index = i
            elif nums[i] > max2:
                max2 = nums[i]
        
        if max1 >= 2 * max2:
            return index
        return -1