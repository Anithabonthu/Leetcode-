class Solution:
    def tribonacci(self, n: int) -> int:
        d={}
        def func(n):
            if n in d:
                return d[n]
            if n==0 or n==1:
                return n
            elif n==2:
                return 1
            else:
                res=func(n-1)+func(n-2)+func(n-3)
                d[n]=res
                return res
            
        return func(n)