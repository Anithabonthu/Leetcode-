class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ind=-1
        maxOnes=-1
        for i in range(len(mat)):
            count=0
            for j in range(len(mat[0])):
                if mat[i][j]:
                    count+=mat[i][j]
            if count > maxOnes:
                maxOnes=count
                ind=i
        return  [ind,maxOnes]
        