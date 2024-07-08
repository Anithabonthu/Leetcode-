# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1,-1]
        points=[]
        prev=head
        current=head.next
        position=1
        while current.next:
            if (current.val >prev.val and current.val>current.next.val) or (current.val <prev.val and current.val<current.next.val):
                points.append(position)
            prev=current
            current=current.next
            position+=1
       
        if len(points)<2:
            return [-1,-1]
        min_value=float('inf')
        max_value=points[-1]-points[0]
        for i in range(1,len(points)):
            min_value=min(min_value,points[i]-points[i-1])
        return [min_value,max_value]
        