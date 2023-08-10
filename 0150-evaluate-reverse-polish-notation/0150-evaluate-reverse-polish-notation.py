## intially we create a stack, then we will iterate through all characters of  the string. since its a 
## Reverse polish notation, the operators will be followed by the numerics, so we will add the numerics first to stack
## then when ever we encounter a operator we will perform the action on the numerics available in stack
## and then we will append the resultant numeric back to the stack and the process follows 
## at end, once the loop is exited, we will return the stack[0] index element 





class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for c in tokens:
            if c == '+':
                stack.append(stack.pop()+stack.pop())
                
            elif c == '-':
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif c == '*':
                stack.append(stack.pop()*stack.pop())
            elif c == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
        