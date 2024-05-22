# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return head
        temp=head
        stack=[]
        while temp:
            stack.append(temp.val)
            temp=temp.next
        max_sum=0
        c=0
        while stack:
            c=stack.pop(0)+stack.pop()
            if c>max_sum:
                max_sum=c
        return max_sum
        