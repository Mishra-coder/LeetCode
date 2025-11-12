class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    if nums[m] == target:
                        ans = m
                    r = m - 1
                else:
                    l = m + 1
            return ans
        
        def last():
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    if nums[m] == target:
                        ans = m
                    l = m + 1
                else:
                    r = m - 1
            return ans
        
        return [first(), last()]
