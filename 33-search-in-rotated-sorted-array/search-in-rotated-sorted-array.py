from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int, left: int, right: int):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return n - 1

        tmp = nums.index(min(nums))

        res = -1
            
        if tmp == 0:
            return self.binary_search(nums, target, 0, n - 1)
            
        if target >= nums[0]:
            res = self.binary_search(nums, target, 0, tmp - 1)
            return res

        if target <= nums[-1]:
            res = self.binary_search(nums, target, tmp, n - 1)
            return res
        
        return res
