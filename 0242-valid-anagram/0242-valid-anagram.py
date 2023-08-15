## Question:- check if the given strings has same characters.

## 1.First if the lenght of given two strings are not equal then it is not a anagram.
## 2.Create an array with 0's of length 256 [ beacuse 256 are the possible asci values]
## 3. traverse through the lenght of any string and store the one asci with +values
## 4. and other string ascii with - values, so the matching characters will get nullified.
## 5. if the resultant array has 0 then it is anagram.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        a = [0]* 256
        
        for i in range(len(s)):
            a[ord(s[i])] += 1
            a[ord(t[i])] -= 1
        
        for x in a:
            if x != 0:
                return False
        return True
            