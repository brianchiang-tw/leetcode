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

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        single_num = 0
        
        # compute single number by bit masking
        for bit_shift in range(32):
            
            sum = 0
            
            for number in nums:
                
                # collect the bit sum
                sum += ( number >> bit_shift ) & 1

            # Extract bit information of single number by modulo
            # Other number's bit sum is removed by mod 3 (i.e., all other numbers appear three times)
            single_num |= ( sum % 3 ) << bit_shift
            
            
        
        if ( single_num & (1 << 31) ) == 0:
            return single_num
        else:
            return -( (single_num^(0xFFFF_FFFF))+1 )



# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of dictionary building, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


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
