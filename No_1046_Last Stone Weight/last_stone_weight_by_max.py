'''

Description:


We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

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



from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        
        while len(stones) > 1:
            
            # get first large element
            first = max( stones )
            
            stones.remove(first)
            
            # get second large element
            second = max( stones )
            
            # compute the difference
            diff = first-second
            
            if diff:
                stones[ stones.index(second) ] = diff
            else:
                stones.remove(second)
            
        return sum(stones)



# n : the length of input array, stones

## Time Complexity: O( n^2 )
#
# The overhead in time is the while loop iterating on len(stones), which is of O( n ),
# amd the cost of max( stones ), which is of O( n ) also.
#
# It takes O( n^2 ) in total.


## Space Complexity: O( 1 )
#
# The overhead in space is the temporary variable for stone merging, which is of O( 1 ).



def test_bench():

    test_data = [
                    [2,7,4,1,8,1],
                    [10,20,15,8,5]
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