'''

Description:

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]



Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9

Hint #1  
Generate all numbers with sequential digits and check if they are in the given range.

Hint #2  
Fix the starting digit then do a recursion that tries to append all valid digits.

'''


from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        result = []
        
        # scan all possible first digit
        for first_digit in range(1, 10):
            
            cur_num = first_digit
            
            # growing based on first digit
            for next_digit in range(first_digit + 1, 10):
                
				# growing with sequential digit
                cur_num = cur_num * 10 + next_digit
                
                if low <= cur_num <= high:
                    # check current number is in range or not
                    result.append(cur_num)
                    
        return sorted(result)



## Time Complexity: O( 1 )
#
# The overhead in time is the cost of nested iteration, which is of O( C(9, 2) ) = O( 36 ) = O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, whichi is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().sequentialDigits( low = 100, high = 300 )
        self.assertEqual(result, [123,234] )


    def test_case_2( self ):

        result = Solution().sequentialDigits( low=1000, high=13000 )
        self.assertEqual(result, [1234,2345,3456,4567,5678,6789,12345] )


if __name__ == '__main__':

    unittest.main()        