class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.pref = [0]
        for x in nums:
            self.pref.append(self.pref[-1] + x)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.pref[right + 1] - self.pref[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)