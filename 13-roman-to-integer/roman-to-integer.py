class Solution:
    def romanToInt(self, s: str) -> int:
        roman_mapper = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        res=0
        for i in range(len(s)-1):
            if (roman_mapper.get(s[i]) >= roman_mapper.get(s[i+1])):
                res += roman_mapper.get(s[i])
            else:
                res -= roman_mapper.get(s[i])
        
        return res + roman_mapper.get(s[-1])