class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_value = set()
        max_length = 0
        left = 0

        for right in range(len(s)):
            if(s[right] not in set_value):
                set_value.add(s[right])
                max_length = max(right-left+1, max_length)
                continue

            while(s[right] in set_value):
                set_value.discard(s[left])
                left+=1
            set_value.add(s[right])

        return max_length