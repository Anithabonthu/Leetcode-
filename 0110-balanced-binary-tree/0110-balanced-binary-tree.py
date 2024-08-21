# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBal=True
        def check(node):
            if not node:
                return 0
            l=check(node.left)
            r=check(node.right)
            if abs(l-r)>1:
                self.isBal=False
            return max(l,r)+1
        check(root)
        return self.isBal

        