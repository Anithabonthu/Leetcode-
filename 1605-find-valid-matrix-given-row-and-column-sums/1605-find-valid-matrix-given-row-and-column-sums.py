class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROWS,COLS=len(rowSum),len(colSum)
        res=[[0]*COLS for _ in range(ROWS)]
        for r in range(ROWS):
            res[r][0]=rowSum[r]
        for c in range(COLS):
            cur=0
            for r in range(ROWS):
                cur+=res[r][c]
            r=0
            while cur>colSum[c]:
                diff=cur-colSum[c]
                max_shift=min(res[r][c],diff)
                res[r][c]-=max_shift
                res[r][c+1]+=max_shift
                cur-=max_shift
                r+=1
        return res
        