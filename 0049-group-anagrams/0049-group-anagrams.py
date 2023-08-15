## find the strings which has similar characters and return them as single list in a list.

##1.first create a hashmap
##2. Traverse through the list of strings given 
##3. sort the string one by one.
##4. if the sorted string exists as a key then add its unsorted value to the key
##5. else, create a sorted value as key and unsorted value of respective element as its value. 
## Repeat for all strings



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm ={}
        
        for i in strs:
            w =  "".join(sorted(i))
            
            if w in hm:
                hm[w].append(i)
                
            else:
                hm[w] = [i]
        return list(hm.values())