class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        diff = (sumA - sumB) // 2
        
        setB = set(bobSizes)
        
        for a in aliceSizes:
            if a - diff in setB:
                return [a, a - diff]
                