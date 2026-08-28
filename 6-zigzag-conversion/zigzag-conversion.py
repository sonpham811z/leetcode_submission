class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""]*numRows

        current_row = 0
        going_down = False

        for i in s:
            rows[current_row] += i

            if(current_row == 0):
                going_down = not going_down
            if(current_row == numRows-1):
                going_down = not going_down


            if(going_down):
                current_row+=1
            if(not going_down):
                current_row-=1

        res = ""
        for i in rows:
            res+=i
        
        return res
