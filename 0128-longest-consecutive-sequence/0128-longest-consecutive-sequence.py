## We can do this by sorting the elements, but the Time complexity would be O(nlogn), since we are using sorting and 
## Best tc of sorting is merge sort with o(nlogn).


## we will create a set of those nums, so that searching, can be performed in O(1), we will  traverse though the elements, and see if the current element has (n-1) in the list, ex- if curr element is 100, we will look for 99,if 99 is found we skip current element and go to next element, if not the 100 is start of sequence. then we will look for 101 in list if we find it, then we will increase our longsequence variable by 1, and so on then we will take  lonsequence 





class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums) # Search in set is 0(1)
        
        longest = 0
        
        for n in numset:
            
            # checking if the number is start of sequence, if not we will move to another number in list 
            
            if (n-1) not in numset: 
                
                length = 1
                
                while (n+length) in numset:
                    length +=1 
                
                longest = max(longest,length)  
                
        return longest
            
                    
                

        
        
        
        
        
        

        