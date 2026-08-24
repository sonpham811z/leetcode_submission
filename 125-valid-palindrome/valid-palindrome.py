class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(""," ")
        formated_string = ""
        for char in s:
            if char.isalpha() or char.isalnum():
                formated_string += char

        left = 0
        right = len(formated_string) - 1

        while(left < right):
            
            if(formated_string[left] != formated_string[right]):
                return False
            left += 1
            right -=1
        
        return True
        