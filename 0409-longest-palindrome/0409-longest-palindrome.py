class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        ans = 0
        has_odd = False
        
        for count in freq.values():
            if count % 2 == 0:
                ans += count
            else:
                ans += count - 1
                has_odd = True
        
        return ans + 1 if has_odd else ans

            