# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def func(node,minimum,maximum):
            if not node:
                return abs(minimum-maximum)
            minimum=min(minimum,node.val)
            maximum=max(maximum,node.val)
            left=func(node.left,minimum,maximum)
            right=func(node.right,minimum,maximum)
            return max(left,right)
        return func(root,root.val,root.val)
        