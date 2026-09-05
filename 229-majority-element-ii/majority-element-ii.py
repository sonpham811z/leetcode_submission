class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash_table = {}

        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                hash_table[i]+=1
        
        res = []
        for key, value in hash_table.items():
            if value > n/3:
                res.append(key)
        
        return res
        