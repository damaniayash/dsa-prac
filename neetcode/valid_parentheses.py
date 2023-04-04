class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for i in s:

            if i == '(' or i == '{' or i == '[':
                stack.append(i)

            else:
                
                if len(stack) == 0:
                    return False

                elif i == ')':
                    if stack.pop() != '(':
                        return False
                        
                elif i == '}':
                    if stack.pop() != '{':
                        return False

                elif i == ']':
                    if stack.pop() != '[':
                        return False

        if stack == []:
            return True
        return False
            
