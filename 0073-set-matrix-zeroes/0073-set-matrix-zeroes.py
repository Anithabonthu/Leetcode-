class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def RowMatrix(matrix,rows,cols,i):
            for j in range(cols):
                if matrix[i][j]!=0:
                    matrix[i][j]=float('-inf')
        def ColMatrix(arr,r,c,j):
            for i in range(r):
                if arr[i][j]!=0:
                    arr[i][j]=float('-inf')
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(0,rows):
            for j in range(0,cols):
                if matrix[i][j] == 0:
                    RowMatrix(matrix,rows,cols,i)
                    ColMatrix(matrix,rows,cols,j)
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == float('-inf'):
                    matrix[i][j]=0
        