class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array_str = s.strip().split(' ')

        return len(array_str[-1])