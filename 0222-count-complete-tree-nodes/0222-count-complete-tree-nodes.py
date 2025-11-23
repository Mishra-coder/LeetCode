# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        def leftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def rightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        left_h = leftHeight(root)
        right_h = rightHeight(root)

        if left_h == right_h:
            return (1 << left_h) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)