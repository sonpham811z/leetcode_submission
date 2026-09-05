class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_table = {}
        
        # Bước 1: Chỉ giữ lại tối đa 2 ứng viên tiềm năng trong hash_table
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
            
            # Nếu có nhiều hơn 2 ứng viên, giảm bậc tất cả đi 1 đơn vị
            if len(hash_table) > 2:
                new_table = {}
                for key, value in hash_table.items():
                    if value > 1:
                        new_table[key] = value - 1
                hash_table = new_table
                
        # Bước 2: Kiểm tra lại xem các ứng viên còn lại có thực sự > n/3 không
        res = []
        n = len(nums)
        for candidate in hash_table:
            if nums.count(candidate) > n // 3:
                res.append(candidate)
                
        return res
