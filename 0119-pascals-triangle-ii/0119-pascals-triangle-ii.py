class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        
        for k in range(1, rowIndex + 1):
            next_val = row[-1] * (rowIndex - k + 1) // k
            row.append(next_val)
        
        return row
        