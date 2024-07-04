# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next
        n=len(stack)
        i=1
        res=[]
        temp=[]
        while i<n:
            if stack[i]==0:
                res.append(sum(temp))
                temp=[]
            else:
                temp.append(stack[i])
            i+=1
        if not stack:
            return None
        else:
            ptr=None
            while res:
                newnode=ListNode(res.pop())
                newnode.next=ptr
                ptr=newnode
            return ptr