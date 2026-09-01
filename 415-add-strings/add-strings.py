class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i = len(num1)-1
        j = len(num2)-1

        remember = 0
        current = 0

        while(i>=0 or j >= 0 or remember >0):
            sum = remember

            if(i >= 0):
                sum+=int(num1[i])
                i-=1
            if(j>=0):
                sum+=int(num2[j])
                
                j-=1
                

            remember=sum//10
            res+= str(sum%10)
            res = res[-1] + res[:-1]
        
        return res
