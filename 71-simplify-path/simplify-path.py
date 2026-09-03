class Solution:
    def simplifyPath(self, path: str) -> str:
        array_str = path.split("/")
        print(array_str)
        stack = []

        for i in array_str:
            if((len(stack) == 0 and i == '..') or i == '.' or i == ''):
                continue
            if(i != '..'):
                stack.append(i)
            else:
                stack.pop()
        
        res = "/".join(stack)
        return "/" + res