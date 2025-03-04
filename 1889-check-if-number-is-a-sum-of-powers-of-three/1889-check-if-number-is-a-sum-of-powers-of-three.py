class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n==0 or n==1:
            return True
        elif n%3==2:
            return False
        return(self.checkPowersOfThree(n//3))
        