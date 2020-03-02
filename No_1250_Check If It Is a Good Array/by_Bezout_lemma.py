'''

Description:

Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.

 

Example 1:

Input: nums = [12,5,7,23]
Output: true
Explanation: Pick numbers 5 and 7.
5*3 + 7*(-2) = 1



Example 2:

Input: nums = [29,6,10]
Output: true
Explanation: Pick numbers 29, 6 and 10.
29*1 + 6*(-3) + 10*(-1) = 1
Example 3:

Input: nums = [3,6]
Output: false
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9

'''

from typing import List
from math import gcd

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        
        
        # ax + by = 1 has integer solution only when gcd(a, b) == 1
        
        x = nums[0]
        
        for number in nums:
            
            x = gcd(x, number)
            
        
        return x == 1



# k : largest number in input array, nums.
# n : the length of input array, nums.

## Time Complexity: O( n log k )
#
# The overhead in time is the for loop with the cost of gcd.
# The for loop takes O( n ), and the gcd takes O( log k ).
# It takes O( n log k ) in total.

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping variable and temporary variable for computation, which is of O( 1 ).






from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array')
def test_bench():

    test_data = [
                    TestEntry( array = [12,5,7,23] ),
                    TestEntry( array = [29,6,10] ),
                    TestEntry( array = [3,6] )
                ]

    # expected output:
    '''
    True
    True
    False
    '''


    for t in test_data:
        print( Solution().isGoodArray( nums = t.array ) )

    return



if __name__ == '__main__':

    test_bench()