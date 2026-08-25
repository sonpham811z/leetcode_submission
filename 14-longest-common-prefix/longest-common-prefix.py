class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first_string = strs[0]

        for i, char in enumerate(first_string):
            for other_str in strs[1:]:
                if(i >= len(other_str) or other_str[i] != char):
                    return first_string[:i]
        
        return first_string

            