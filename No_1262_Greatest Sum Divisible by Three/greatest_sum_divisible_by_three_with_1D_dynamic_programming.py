'''

Description:

Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).



Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.



Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4

'''


from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        # a record to max sum, for remainder 0, 1, 2 in module 3 system
        max_sum_dp = {0:0, 1:0, 2:0}
        
        for number in nums:
            
            # backup previous state of max_sum_dp
            prev_state = max_sum_dp.copy()
            
            for remainder in range(3):
            
                summation = prev_state[remainder] + number
                
                update_index = summation % 3
                
                max_sum_dp[update_index] = max( summation, max_sum_dp[update_index])
            
        
        return max_sum_dp[0]
        
            
    
# n : the number of input array, nums.

## Time Complexity : O( n )
#
# The overhead in time is the for loop, iterating on number, which is of O( n ).


## Space Complexity: O( 1 )
#
# The overhead in space is the storage for dictionary, max_sum_dp as well as prev_state,
# which is of O( 3 + 3 ) = O( 6 ) = O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence_of_integer')
def test_bench():

    test_data = [
                    TestEntry([3,6,5,1,8]),
                    TestEntry([4]),
                    TestEntry([1,2,3,4,4])
                ]        
    
    for t in test_data:

        print( Solution().maxSumDivThree(t.sequence_of_integer) )
    
    return



if __name__ == '__main__':

    test_bench()