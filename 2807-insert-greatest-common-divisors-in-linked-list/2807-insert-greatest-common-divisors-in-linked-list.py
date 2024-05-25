# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp=head
        while temp.next:
            data=math.gcd(temp.val,temp.next.val)
            newnode=ListNode(data)
            ptr=temp.next
            temp.next=newnode
            newnode.next=ptr
            temp=ptr
        return head

        