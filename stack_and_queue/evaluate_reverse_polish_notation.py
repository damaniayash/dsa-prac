from collections import deque

class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ['+','-','*','/']
        stack = deque([])
        
        for token in tokens:
            
            if token in operators:
                stack.append(self.calculator(stack.pop(), stack.pop(), token))
                
            else: 
                stack.append(int(token))
                
        return stack.pop()
    
    def calculator(self, operand1, operand2, operator):
        
        if operator == '+':
            return operand2 + operand1
        
        elif operator == '-':
            return operand2 - operand1
        
        elif operator == '*':
            return operand2 * operand1
        
        else:
            return int(operand2 / operand1)
        
        
        