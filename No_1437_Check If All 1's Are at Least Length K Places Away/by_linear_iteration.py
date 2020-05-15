'''

Description:

Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

 

Example 1:



Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.



Example 2:



Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.



Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true



Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true
 

Constraints:

1 <= nums.length <= 10^5
0 <= k <= nums.length
nums[i] is 0 or 1

'''


from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        if k == 0:
            # Quick acception when k = 0
            return True
        
        # record previous index of 1
        prev_position = None
        
        
        
        
        for idx, number in enumerate(nums):
            
            if number == 1:
                
                if ( prev_position is not None ) and ( idx - prev_position ) <= k:
                    # Reject when distance to previous 1 is too close
                    return False
                
                prev_position = idx
        
        # Accept if all 1s are separated of distance k
        return True
                    


# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the cost of loop index, and temporary variable, which is of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence K')

def test_bench():

    test_data = [
                    TestEntry( sequence = [1,0,0,0,1,0,0,1], K = 2 ),
                    TestEntry( sequence = [1,0,0,1,0,1], K = 2 ),
                    TestEntry( sequence = [1,1,1,1,1], K = 0 ),
                    TestEntry( sequence = [0,1,0,1], K = 1 ),
                ]

    # expected output:
    '''
    True
    False
    True
    True
    '''

    for t in test_data:

        print( Solution().kLengthApart( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()