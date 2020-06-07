'''

Description:

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.



Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]



Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

'''


from typing import List
from random import randint
from bisect import bisect_right

class Solution:

    def __init__(self, w: List[int]):
        
        # built a weight accumulation table
        # acc[0] = w[0], for i = 0
        # acc[i] = acc[i-1]+w[i] for i = 1 ~ (n-1)
        self.accumulation = w
        
        for i in range(1, len(w)):
            self.accumulation[i] = self.accumulation[i-1] + w[i]

            
            
    def pickIndex(self) -> int:
        
        sum_of_all_weight = self.accumulation[-1]
        
        # generate a random value from 1 to ( sum of all weight - 1 )
        random_value = randint(0, sum_of_all_weight-1)
        
        # mapping the random value to its corresponding index with w[i]
        point = bisect_right(self.accumulation, random_value)
        
        return point
    
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()



# n : the length of input array, w.

## Time Complexity: O( log n )
#
# The overhead in time is the cost of bisection (i.e., variation of binary search), which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for accumulation table, in-place with w, which is of O( 1 )


'''

Note:

The output is non-deterministic, therefore test bench is not provided.

'''