class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prevRows = self.generate(numRows -1)
        prevRow = prevRows[-1]
        currRow = [1]

        for i in range(1, numRows -1):
            currRow.append(prevRow[i-1] + prevRow[i])
        
        currRow.append(1)
        prevRows.append(currRow)

        return prevRows
        