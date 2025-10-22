class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def backtrack(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == target else 0
            add = backtrack(i + 1, curr_sum + nums[i])
            subtract = backtrack(i + 1, curr_sum - nums[i])
            
            return add + subtract
        
        return backtrack(0, 0)
