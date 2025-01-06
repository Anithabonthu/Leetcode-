class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows==0:
            return []
        elif numRows==1:
            return [[1]]
        prev_rows=self.generate(numRows-1)
        last=prev_rows[-1]
        current_row=[1]
        for i in range(1,numRows-1):
            current_row.append(last[i]+last[i-1])
        current_row.append(1)
        prev_rows.append(current_row)

        return prev_rows

        