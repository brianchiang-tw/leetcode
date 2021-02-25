'''

Description:

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].



Example 2:

Input: nums = [1,2,3,4]
Output: 2



Example 3:

Input: nums = [1,1,1,1]
Output: 0
 

Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109

'''


from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        ## dictionary
        # key: number
        # value: occurrence of number
        number_occ_dict = Counter(nums)
        
        # maximal harmonoius subsequence length, initialized to 0
        max_length = 0
        
        # scan each distinct number
        for number in number_occ_dict:

            # if (number - 1) exists
            if (number - 1) in number_occ_dict:

                # compute current harmonoius subsequence length, made by number and (number-1)
                cur_harmonious_length = number_occ_dict[ number ] + number_occ_dict[ number-1 ]

                # update maximal harmonoius subsequence length
                max_length = max(max_length, cur_harmonious_length)
                
                
        return max_length



## Time Complexity: O( n )
#
# The overhead in time is the cost of Counter as well as iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for Counter, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findLHS( nums=[1,3,2,2,5,2,3,7] )
        self.assertEqual(result, 5 )


    def test_case_2( self ):

        result = Solution().findLHS( nums=[1,2,3,4] )
        self.assertEqual(result, 2 )


    def test_case_3( self ):

        result = Solution().findLHS( nums=[1,1,1,1] )
        self.assertEqual(result, 0 )

if __name__ == '__main__':

    unittest.main()        