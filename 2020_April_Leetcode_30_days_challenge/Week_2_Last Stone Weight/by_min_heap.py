'''

Description:

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

'''



import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # flip the sign, the largest one will become the smallest one
        for i in range( len(stones) ):
            stones[i] *= -1
        
        
        # build the min heap of stones
        heapq.heapify( stones )
        
        while len(stones) > 1:
            
            # get the first largest stone
            first = heapq.heappop( stones )
            
            # get the second largest stone
            second = heapq.heappop( stones )
            
            # compute the difference of stone weight
            diff = first-second
    
            # push back if difference is non-zero
            if diff != 0:
                heapq.heappush( stones, diff )
                             
        # Accpet if min heap is empty.
        # Otherwise, reject.                
        if len(stones):
            return -stones[0]
        else:
            return 0



# n : the length of input array, stones

## Time Complexity: O( n log n)
#
# The overhead in time is the heap maintainance, which is of O( n log n ).

## Space Complexity: O( n )
#
# The overhead in space is the min-heap, which is of O( n ).



def test_bench():

    test_data = [
                    [2,7,4,1,8,1],
                    [10,20,15,8,5],
                ]


    # expected output:
    '''
    1
    2
    '''

    for stone_sequence in test_data:

        print( Solution().lastStoneWeight(stone_sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()
