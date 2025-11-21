class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = [s] * 26
        last = [-1] * 26
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = max(last[idx], i)
        
        ans = 0

        for c in range(26):
            if first[c] < last[c]:
                seen_middle = set()
                for i in range(first[c] + 1, last[c]):
                    seen_middle.add(s[i])
                ans += len(seen_middle)
        
        return ans
        