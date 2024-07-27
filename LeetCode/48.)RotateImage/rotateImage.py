class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # gets columns 
        def get_columns(matrix):
            return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        a=get_columns(matrix)

        tmp = []
        # add the columns in reverse order to tmp
        for i in range(len(matrix)):
            for j in range(len(matrix[i])-1,-1,-1):
                tmp.append(a[i][j])
                print(a[i][j])
                
        # go in order of the matrix and swap out values
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=tmp.pop(0)