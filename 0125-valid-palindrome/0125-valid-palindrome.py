
# ## One approach but we will be using isalnum function and creating an extra space by creating new string.
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newstr = ""
        
#         for i in s:
#             if i.isalnum():
#                 newstr += i.lower()
        
#         return newstr == newstr[::-1]
    

    
    
## 2nd Approach:- in this solution we leverage ascii values, first we iterate through the each characters from end and beginning using two pointer, and run loop until l<r
## also, in the loop we will see if the current character is not alphnumeric, then we will move the pointer position until , we reach alphanumeric character.
## will do same for l and r,  and if we found both left.lower and right.lower not equal to each other then we will return false.
## if its equal then we increment l and decrement r

class Solution:
    def isPalindrome(self, s: str) -> bool:  
        l, r = 0, len(s) - 1
        while l < r :
            
            while l < r and not self.alphanum(s[l]): # so when we encounter any non alphanumerical values we move our pointer to next 
                l+= 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower() :
                return False
            
            l+=1
            r-=1
            
        return True
    
    def alphanum(self, c):  ## creating a function to check if a current character is a alphanumerical using ascii values
        return (
            ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9')
               )

