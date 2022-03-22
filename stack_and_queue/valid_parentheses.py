from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                
                elif i == ']':
                    if stack.pop() != '[':
                        return False
                    
                elif i == ')':
                    if stack.pop() != '(':
                        return False
                    
                elif i == '}':
                    if stack.pop() != '{':
                        return False
                    
        if len(stack) == 0: return True
        else: return False
        
        # stack = deque()
        # for i in s:
        #     if i == '(' or i == '[' or i == '{':
        #         stack.append(i)
        #     elif i == ']':
        #         if len(stack) == 0:
        #             return False
        #         if stack.pop() != '[':
        #             return False
        #     elif i == ')':
        #         if len(stack) == 0:
        #             return False
        #         if stack.pop() != '(':
        #             return False
        #     elif i == '}':
        #         if len(stack) == 0:
        #             return False
        #         if stack.pop() != '{':
        #             return False
        # if len(stack) == 0: return True
        # else: return False
            
                