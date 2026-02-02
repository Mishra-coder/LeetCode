# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            node = TreeNode(nums[m])
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node
        
        return build(0, len(nums) - 1)
