## The problem is, we need to find the warm temperature after the given day temperature and how long it took from a given ## day to get a warm temperature

##  while iterating through the given temp array, we will see if the temp is higher than the stack[top] if so then we will pop the existing elements in stack and add the value to result array which current i - stackindx and we will append the temp,i to stack




class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            
            while stack and t > stack[-1][0]: ## [0] beacuse of the temp index in stack 
                
                stackT, stackindx = stack.pop()
                
                res[stackindx] = (i - stackindx)
                
            stack.append([t,i])
        
        return res
        
        
        
        
        
        