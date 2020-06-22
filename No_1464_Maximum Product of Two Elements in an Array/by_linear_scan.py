'''

Description:

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 


Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 



Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.



Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

'''



class Solution(object):
    def maxProduct(self, nums):

        first, second = 0, 0

        for number in nums:

            if number > first:
                # update first largest and second largest
                first, second = number, first

            elif number > second:
                # update second largest
                second = number
        
        return ( first - 1 ) * ( second - 1 )



# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which are of O( 1 ).

import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().maxProduct( nums = [3,4,5,2] )
        self.assertEqual( result, 12 )


    
    def test_case_2(self):

        result = Solution().maxProduct( nums = [1,5,4,5] )
        self.assertEqual( result, 16 )



    def test_case_3(self):
    
        result = Solution().maxProduct( nums = [3,7] )
        self.assertEqual( result, 12 )



if __name__ == '__main__':

    unittest.main()
