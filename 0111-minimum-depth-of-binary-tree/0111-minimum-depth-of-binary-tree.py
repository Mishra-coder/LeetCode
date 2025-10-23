# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not root.left or not root.right:
            return 1 + max(left,right)

        return 1 + min(left,right)

