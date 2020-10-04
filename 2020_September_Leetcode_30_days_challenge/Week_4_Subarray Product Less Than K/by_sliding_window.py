'''

Description:

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.



Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

Hint #1  
For each j, let opt(j) be the smallest i so that nums[i] * nums[i+1] * ... * nums[j] is less than k. opt is an increasing function.

'''


from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            # Quick response for invalid k on product of positive numbers
            return 0
        
        else:
            left_sentry = 0

            num_of_subarray = 0
            product_of_subarry = 1

            # update right bound of sliding window
            for right_sentry in range( len(nums) ):

                product_of_subarry *= nums[right_sentry]

                # update left bound of sliding window
                while product_of_subarry >= k:
                    product_of_subarry //= nums[left_sentry]
                    left_sentry += 1

                # Note:
                # window size = right_sentry - left_sentry + 1

                # update number of subarrary with product < k
                num_of_subarray += right_sentry - left_sentry + 1

            return num_of_subarray


# n : the length of nums

## Time Complexity : O( n )
#
# Each element is visited at most two times, then the cost of time is O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest


class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().numSubarrayProductLessThanK( nums = [10, 5, 2, 6], k = 100 )
        self.assertEqual(result, 8)



if __name__ == '__main__':

    unittest.main()        