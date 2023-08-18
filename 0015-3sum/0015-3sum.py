## T.C - O(n^2)

### since we dont need the repeating numbers to be in the solution we sort the elements and skip the element if its repeating after the first element.

## and then we follow the two sum - 2 approach




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        nums = sorted(nums) ## to avoid repeatation
        
        
        for i, a in enumerate(nums):
            
            if i > 0 and nums[i-1] == nums[i]: ## if we see same element for position a we skip the below loop and continue to next element
                continue 
                
            l,r = i+1, len(nums)-1
            
            while l < r:
                
                threesum = a + nums[l] + nums[r]
                
                if threesum > 0 :
                    
                    r = r-1
                
                elif threesum < 0 :
                    
                    l = l + 1
                
                else:
                    
                    res.append([a,nums[l], nums[r]])
                    
                    l = l+1
                    r = r-1
                    
                    while l<r and  nums[l] == nums[l-1]:
                        l+=1
        return res
            
        