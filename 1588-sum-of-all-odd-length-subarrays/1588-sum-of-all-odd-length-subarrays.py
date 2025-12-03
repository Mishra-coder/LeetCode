class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        total_sum = 0

        for i, val in enumerate(arr):
            total = (i + 1) * (n - i)     
            odd = (total + 1) // 2      
            total_sum += val * odd       

        return total_sum