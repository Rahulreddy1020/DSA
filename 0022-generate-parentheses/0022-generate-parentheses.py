### here we have 3 conditions
### left and right should be equal to given n then add it to result from stack
### left should be added only when its less than n 
### right should be added when it is less than left


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def fun(left,right):
            
            if left == right == n:
                res.append("".join(stack))
                return 
            
            if left < n:
                stack.append('(')
                fun(left+1,right)
                stack.pop()
            
            if right < left:
                
                stack.append(')')
                fun(left,right+1)
                stack.pop()
                
        fun(0,0)
        return res
                
        