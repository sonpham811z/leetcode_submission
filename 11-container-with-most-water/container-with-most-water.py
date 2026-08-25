class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container = 0
        left = 0
        right = len(height) - 1

        while(left < right):
            s = min(height[left], height[right]) * abs(right-left)
            max_container = max(s, max_container)

            if(height[left] >= height[right]):
                right-=1
            else:
                left+=1
        
        return max_container