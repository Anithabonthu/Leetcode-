class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res=0
        for m in range(1,len(rating)-1):
            left_small=right_large=0
            for i in range(m):
                if rating[i]<rating[m]:
                    left_small+=1
            for i in range(m+1,len(rating)):
                if rating[i]>rating[m]:
                    right_large+=1
            res+=left_small*right_large
            
            left_larger=m-left_small
            right_small=len(rating)-1-m-right_large
            res+=left_larger*right_small
        return res
        