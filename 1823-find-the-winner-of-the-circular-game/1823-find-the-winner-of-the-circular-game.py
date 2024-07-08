class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        temp=[num for num in range(1,n+1)]
        current_index=0
        while len(temp)!=1:
            remove_ele=(current_index+k-1)%len(temp)
            temp.pop(remove_ele)
            current_index=remove_ele
        return temp[0]
        