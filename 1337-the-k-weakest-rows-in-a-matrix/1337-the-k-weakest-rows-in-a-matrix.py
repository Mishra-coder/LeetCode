class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        arr = []

        for i in range(len(mat)):
            soldiers = sum(mat[i])
            arr.append((soldiers, i))

        arr.sort()

        return [idx for soldiers, idx in arr[:k]]
        