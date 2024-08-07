# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        q=[]
        level=0
        q.append(root)
        while q:
            size=len(q)
            v=[]
            while size>0:
                size-=1
                node=q.pop(0)
                v.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level%2==1:
                v=v[::-1]
            level+=1
            ans.append(v)
        return ans
        