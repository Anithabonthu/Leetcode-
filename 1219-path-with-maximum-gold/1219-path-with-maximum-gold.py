class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c,visit):
            if(min(r,c)<0 or r==rows or c==cols or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            res=grid[r][c]
            neighbours=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr,nc in neighbours:
                res=max(res,grid[r][c]+dfs(nr,nc,visit))
            visit.remove((r,c))
            return res
        res=0
        for r in range(rows):
            for c in range(cols):
                res=max(res,dfs(r,c,set()))
        return res

        