class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        distance = 0
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = i
            else:
                distance = abs(hash_table[nums[i]] - i)
                if(distance <= k):
                    return True
                else:
                    hash_table[nums[i]] = i

        return False
