class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        low, high = 0, len(s)
        ans = []

        for ch in s:
            if ch == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1

        ans.append(low)
        return ans
        