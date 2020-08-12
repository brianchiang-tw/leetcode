'''

Description:

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].



Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9

'''



class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        odd_lowerbound, odd_upperbound = -1, -1
        
        # compute smallest odd number in range
        if low % 2 == 1:
            odd_lowerbound = low
        else:
            odd_lowerbound = low + 1
        
        # compute largest odd number in range
        if high % 2 == 1:
            odd_upperbound = high
        else:
            odd_upperbound = high - 1
            
        
        # compute the number of odd numbers in range
        return (odd_upperbound - odd_lowerbound) // 2 + 1


## Time Complexity: O( 1 )
#
# The overhead in time is the cost of boundary computation, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().countOdds(low = 3, high = 7)
        self.assertEqual(result, 3)


    def test_case_2( self ):
    
        result = Solution().countOdds(low = 8, high = 10)
        self.assertEqual(result, 1)        


if __name__ == '__main__':

    unittest.main()