class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet_target = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                current_target = nums[i] + nums[left] + nums[right]
                if(current_target == target):
                    return current_target
                
                if(abs(current_target-target) < abs(closet_target-target)):
                    closet_target = current_target

                if(current_target > target):
                    right -= 1
                
                if(current_target < target):
                    left += 1
        return closet_target