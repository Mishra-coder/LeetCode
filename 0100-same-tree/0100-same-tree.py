# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # print(p)
        # print(q)
        found=[True]
        ans=self.check(p,q,found)
        return ans[0]
    def check(self,p,q,found):
        if p is None and q is None:
            # print("p",p)
            
            return found

        elif (p is None and q is not None) or (q is None and p is not None):
            # print(p)
            found[0]=False
            return found

        elif p.val!=q.val:
            found[0]=False
            return found

       
        self.check(p.left,q.left,found)
            
        self.check(p.right,q.right,found)
        
        return found
            

        