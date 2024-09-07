# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def helper(list,node):
            if not list:
                return True
            if not node or node.val != list.val:
                return False
            return helper(list.next,node.left) or  helper(list.next,node.right)
        if not root:
            return False
        if helper(head,root):
            return True
        return self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
        