'''

Description:

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3



Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

'''



from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        num_occ_dict = Counter( nums )
        
        return [ number for number in num_occ_dict if num_occ_dict[number] == 1][0]



# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of dictionary building, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().singleNumber( [2,2,3,2] )
        self.assertEqual( result, 3)


    
    def test_case_2(self):
    
        result = Solution().singleNumber( [0,1,0,1,0,1,99] )
        self.assertEqual( result, 99)
    


if __name__ == '__main__':

    unittest.main()
