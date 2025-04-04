class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
      
        rows=len(matrix)
        cols=len(matrix[0])
        arr=[[0 for i in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                arr[i][j]=matrix[j][i]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j]=arr[i][j]
        
        #print(matrix)
        for i in range(rows):
            matrix[i]=matrix[i][::-1]
        