# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find(node):
            l=0
            while node:
                l+=1
                node=node.next
            return l
        if not head or not head.next:
            return
        length=find(head)
        mid=length//2
        count=0
        temp=head
        while count!=mid-1:
            count+=1
            temp=temp.next
        temp.next=temp.next.next
        return head