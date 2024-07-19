class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix)
        cols=len(matrix[0])
        res=[]
        rowMin=[]
        colsMax=[]
        for i in range(rows):
            rmin=float('inf')
            for j in range(cols):
                rmin=min(rmin,matrix[i][j])
            rowMin.append(rmin)
        for i in range(cols):
            cmax=0
            for j in range(rows):
                cmax=max(cmax,matrix[j][i])
            colsMax.append(cmax)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==rowMin[i] and matrix[i][j]==colsMax[j]:
                    res.append(matrix[i][j])
        return res
        