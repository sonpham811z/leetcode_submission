class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_set = set()
        col_set = set()

        row = len(matrix)
        col = len(matrix[0])        

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        print(row_set)
        print(col_set)
        for i in range(row):
            for j in range(col):
                print(i,j,"concac")
                if i in row_set or j in col_set:
                    print(i,j)
                    matrix[i][j] = 0
        return matrix