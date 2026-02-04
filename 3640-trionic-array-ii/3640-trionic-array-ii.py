class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)
        if n < 4:
            return 0
        
        inf = float('inf')
        
        inc_fwd = [-inf] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_fwd[i] = nums[i] + nums[i-1]
                if i > 1 and inc_fwd[i-1] != -inf:
                    inc_fwd[i] = max(inc_fwd[i], nums[i] + inc_fwd[i-1])
        
        mountain = [-inf] * n
        for i in range(2, n):
            if nums[i] < nums[i-1]:
                if inc_fwd[i-1] != -inf:
                    mountain[i] = max(mountain[i], nums[i] + inc_fwd[i-1])
                if mountain[i-1] != -inf:
                    mountain[i] = max(mountain[i], nums[i] + mountain[i-1])
                    
        inc_suffix = [-inf] * n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                inc_suffix[i] = nums[i] + nums[i+1]
                if i < n-2 and inc_suffix[i+1] != -inf:
                    inc_suffix[i] = max(inc_suffix[i], nums[i] + inc_suffix[i+1])
        
        ans = -inf
        for q in range(2, n-1):
            if mountain[q] != -inf and inc_suffix[q] != -inf:
                ans = max(ans, mountain[q] + inc_suffix[q] - nums[q])
        
        return int(ans) if ans != -inf else 0