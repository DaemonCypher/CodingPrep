class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def generate( numRows: int) -> List[List[int]]:
            if numRows == 0:
                return []
            if numRows == 1:
                return [[1]]
            
            prevRows = generate(numRows - 1)
            newRow = [1] * numRows
            
            for i in range(1, numRows - 1):
                newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
                
            
            prevRows.append(newRow)
            return prevRows
        pascal = generate(rowIndex+1)

        return pascal[-1]