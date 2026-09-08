class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        res = []
        for i in range(n):
            row = [0]*n
            res.append(row)

        left = 0
        right = n-1
        top = 0
        bottom = n-1
        count = 1
        while left <= right and top <= bottom:
            #left to right
            for i in range(left, right+1, 1):
                res[top][i] = count
                count+=1
            top+=1

            #top to bottom
            for i in range(top, bottom+1, 1):
                res[i][right] = count
                count+=1
            right-=1

            if top<=bottom:
                for i in range(right, left-1, -1):
                    res[bottom][i] = count
                    count+=1
                bottom-=1
            
            if left<=right:
                for i in range(bottom, top-1, -1):
                    res[i][left] = count
                    count+=1
                left+=1

        return res
            