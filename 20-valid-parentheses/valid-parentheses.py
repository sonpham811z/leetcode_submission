class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack_open = []

        for i in s:
            if (i == '(' or i == '[' or i == '{'):
                stack_open.append(i)
            else:
                if not stack_open:
                    return False

                if(i == ')'):
                    if(stack_open.pop() != '('):
                        return False
                if(i == ']'):
                    if(stack_open.pop() != '['):
                        return False
                if(i == '}'):
                    if(stack_open.pop() != '{'):
                        return False 
        
        return not stack_open