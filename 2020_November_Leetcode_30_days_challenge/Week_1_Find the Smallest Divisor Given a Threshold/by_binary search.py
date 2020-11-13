'''

Description:

Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 



Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3



Example 3:

Input: nums = [19], threshold = 5
Output: 4
 

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6

'''


from typing import List
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        # ------------------------
        
        ## Verify current dividend is valid or not
        
        def check_in_range(dividend):
            
            summation = sum( ceil(number/dividend) for number in nums )
            
            return summation <= threshold
        
        # ------------------------
        
        ## Use binary search to approximate minimal valid dividend
        
        left, right = 1, max(nums)
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if check_in_range(dividend=mid):
                # current dividend is valid, try to make it smaller
                right = mid - 1
            
            else:
                # current dividend is invalid, try to make it bigger
                left = mid + 1
                
        return left


# n : the length of nums
# m : the value of threshold

## Time Complexity: O( n log m )
#
# The overhead in time is the cost of binary search with linear for-loop, which is of O( n log m )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().smallestDivisor( nums=[1,2,5,9], threshold=6 )
        self.assertEqual(result, 5)


    def test_case_2( self ):

        result = Solution().smallestDivisor( nums=[2,3,5,7,11], threshold=11 )
        self.assertEqual(result, 3)


    def test_case_3( self ):

        result = Solution().smallestDivisor( nums=[19], threshold=5 )
        self.assertEqual(result, 4)


if __name__ == '__main__':

    unittest.main()
