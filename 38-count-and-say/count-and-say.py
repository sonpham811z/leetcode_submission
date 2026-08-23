class Solution:
    def countAndSay(self, n: int) -> str:
        res="1"
        for _ in range(n - 1):
            next_res = []
            count = 1
            
            for j in range(len(res)):
                if j + 1 < len(res) and res[j] == res[j + 1]:
                    count += 1
                else:
                    next_res.append(str(count))
                    next_res.append(res[j])
                    count = 1
            
            res = "".join(next_res)
            
        return res

