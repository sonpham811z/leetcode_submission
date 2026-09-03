class Solution:
    def simplifyPath(self, path: str) -> str:
        array_str = path.split("/")
        print(array_str)
        stack = []

        for i in array_str:
            if((len(stack) == 0 and i == '..') or i == '.' or i == ''):
                print("cc1")
                continue
            if(i != '..'):
                print("cc2")
                stack.append(i)
            else:
                print("cc3")
                stack.pop()
        
        res = "/".join(stack)
        return "/" + res