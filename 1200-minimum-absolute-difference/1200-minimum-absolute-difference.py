class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        mn = float('inf')
        ans = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]

            if diff < mn:
                mn = diff
                ans = [[arr[i - 1], arr[i]]]
            elif diff == mn:
                ans.append([arr[i - 1], arr[i]])

        return ans
        