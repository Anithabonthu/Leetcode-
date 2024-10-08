# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA=headA
        pointerB=headB
        while pointerA!=pointerB:
            pointerA=headB if not pointerA else pointerA.next
            pointerB=headA if not pointerB else pointerB.next
        return pointerA 
        