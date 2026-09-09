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
        
        # 1. Check nhanh các vị trí biên an toàn
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return n - 1

        # FIX TRIỆT ĐỂ TẠI ĐÂY: Tìm chính xác chỉ số của phần tử nhỏ nhất (điểm xoay tmp)
        # Thay vì co 2 đầu bừa bãi, ta dùng hàm min() của Python lấy chỉ số chuẩn 100%
        tmp = nums.index(min(nums))

        res = -1
            
        # 2. Nếu mảng không bị xoay (thằng nhỏ nhất nằm ở đầu)
        if tmp == 0:
            return self.binary_search(nums, target, 0, n - 1)
            
        # 3. Nếu mảng bị xoay, chia mảng dựa trên điểm xoay chuẩn vừa tìm được
        if target >= nums[0]:
            res = self.binary_search(nums, target, 0, tmp - 1)
            return res

        if target <= nums[-1]:
            res = self.binary_search(nums, target, tmp, n - 1)
            return res
        
        return res
