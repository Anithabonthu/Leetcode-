# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(node,data,path):
            if node.val==data:
                return True
            if node.left and find(node.left,data,path):
                path+="L"
            elif node.right and find(node.right,data,path):
                path+="R"
            return path
        s,d=[],[]
        find(root,startValue,s)
        find(root,destValue,d)
        while len(s) and len(d) and s[-1]==d[-1]:
            s.pop()
            d.pop()
        return "".join("U"*len(s))+"".join(reversed(d))
        