class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        poiter = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                print(nums[poiter], nums[i])
                nums[poiter] = nums[i]
                poiter+=1
        print(poiter)
        return poiter