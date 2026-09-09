class Solution:
    def backtrack(self, remain, comb, start, res, candidates):
        if remain == 0:
            res.append(list(comb))
            return
        
        for index in range(start, len(candidates)):
            value = candidates[index]
            if  value > remain:
                break
            
            comb.append(value)
            self.backtrack(remain-value, comb, index, res, candidates)

            comb.pop()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtrack(target,  [], 0, res, candidates)
        return res
