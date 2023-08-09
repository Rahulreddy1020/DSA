/// Minimum value from a stack can be taken in O(1) time by creating a another stack which maintains the current minimum value
/// while pushing a value to minstack, we compare the value and the minstack[-1], whichever is min we will push that value, like this we will have a minimum value with O(1) time.



class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
       
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)


    def pop(self) -> None:
        
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
