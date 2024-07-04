# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l=[]
        def Inorder(l,node):
            if node:
                Inorder(l,node.left)
                l.append(node.val)
                Inorder(l,node.right)
        if not root:
            return None
        node=root
        Inorder(l,node)
        ptr=None
        while l:
            newnode=TreeNode(l.pop())
            newnode.right=ptr
            ptr=newnode
        return ptr

        