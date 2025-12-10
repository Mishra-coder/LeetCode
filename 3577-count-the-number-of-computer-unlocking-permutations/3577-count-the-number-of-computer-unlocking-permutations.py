class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        prefix_min = complexity[0]
        for i in range(1, n):
            if prefix_min >= complexity[i]:
                return 0
            if complexity[i] < prefix_min:
                prefix_min = complexity[i]
        res = 1
        for x in range(2, n):
            res = (res * x) % MOD
        return res
