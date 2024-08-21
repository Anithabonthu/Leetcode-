# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def func1(node):
            if not node:
                return 0
            left_sum=func1(node.left)
            right_sum=func1(node.right)
            temp=abs(left_sum-right_sum)
            self.ans+=temp
            return left_sum+right_sum+node.val
        func1(root)
        return self.ans