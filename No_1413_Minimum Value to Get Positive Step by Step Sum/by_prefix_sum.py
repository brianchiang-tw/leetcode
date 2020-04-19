'''

Description:

Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

 

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
                step by step sum
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2


                  
Example 2:

Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive. 



Example 3:

Input: nums = [1,-2,-3]
Output: 5
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100

'''



from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        prefix_sum = 0
        negative_most_offset = float('inf')
        
        # linear scan, and update nagative most offset by prefix sum
        for i in range(0, len(nums)):
            
            prefix_sum += nums[i]
            negative_most_offset = min( prefix_sum, negative_most_offset)
        
        # compute the minimum value to get positive
        threshold = min( negative_most_offset,  0 )
        
        # abs to flip the sign, +1 to make it larger than zero
        return abs(threshold)+1



## time complexity: O( n )
#
# The overhead in time isthe cost of linear scna, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable for computation, which are of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [-3,2,-3,4,2] ),
                    TestEntry( sequence = [1,2] ),
                    TestEntry( sequence = [1,-2,-3] ),
                    TestEntry( sequence = [-5] ),
                    TestEntry( sequence = [9] ),
                ]        

    # expected output:
    '''
    5
    1
    5
    6
    1
    '''

    for t in test_data:

        print( Solution().minStartValue( nums = t.sequence) )

    return



if __name__ == '__main__':     
    
    test_bench()