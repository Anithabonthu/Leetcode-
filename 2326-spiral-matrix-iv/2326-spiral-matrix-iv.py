# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ele=[]
        while head:
            ele.append(head.val)
            head=head.next
        matrix=[[-1 for _ in range(n)] for _ in range(m)]
        top,left=0,0
        bottom,right=m-1,n-1
        while top <= bottom and left <= right and ele:
            for i in range(left,right+1):
                if ele:
                    matrix[top][i]=ele.pop(0)
            top+=1
            for i in range(top,bottom+1):
                if ele:
                    matrix[i][right]=ele.pop(0)
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    if ele:
                        matrix[bottom][i]=ele.pop(0)
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    if ele:
                        matrix[i][left]=ele.pop(0)
                left += 1
        return(matrix)
            