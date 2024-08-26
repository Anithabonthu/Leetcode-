"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            for n in node.children:
                dfs(n)
            ans.append(node.val)
        if not root:
            return []
        ans=[]
        dfs(root)
        return ans

        