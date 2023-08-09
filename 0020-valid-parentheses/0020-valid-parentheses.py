/// intially we will traverse through the given string, if the string has a character which matches with the key(which is closing brackets) of the hash map 
/// then we will check if the stack[-1] which is top element, has any open bracket, if so then we will pop the item. the loop will exit when it sees a open bracket,
/// then we will append that item to stack and again traverse throught the string, at last we will return true if only the stack is empty and matches open and close in order.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {'}':'{',')':'(',']':'['}

        for c in s:
            if c in hm:
                if stack and stack[-1] == hm[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
