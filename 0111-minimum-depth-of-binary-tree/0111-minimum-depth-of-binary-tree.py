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
        q=deque([root])
        count=1

        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left ==None and node.right==None:
                    return count

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            count+=1
        return count