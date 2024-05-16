# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                return node.val
            l=dfs(node.left)
            r=dfs(node.right)
            if node.val==3:
                if l==1 and r==1:
                    return 1
                else:
                    return 0
            if node.val==2:
                if l==0 and r==0:
                    return 0
                else:
                    return 1
            return node.val
        data=dfs(root)
        if data==1:
            return True
        return False        