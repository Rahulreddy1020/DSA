## Q - Find the k most repeating elements
## T.c of below Solution o(n)

## Approach: 1. Following a Bucket sort algorith
## having an index we will store the list of elements in the index value,
##lets say we have an element which is repeating 3 times, we will store this value in index 3,
## and if we have another element which is repeating the same 3 times then we will maintain an list of those,
## elements in the index position.
## once we form the list, we will traverse in a reverse order to find the k elements, the reason for reverse is
## having the higher elements on the right.
## then we will store those elements in a list when the len(list) == k we will exit and returnt the list.

## this can be also solved using heap in klogn t.c


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        