'''

Description:

Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

 

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.



Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.



Example 3:

Input: num = 123
Output: 12
 

Constraints:

0 <= num <= 10^6

'''

class Solution():

    def numberOfSteps(self, num: int) -> int:

        step = 0

        while num != 0:

            step += 1

            if num & 1 == 1:
                # odd number, subtract by 1
                num -= 1

            else:
                # even number, divide by 2 <=> right shift one bit
                num >>= 1

        return step


## Time Complexity: O( log n )
#
# The overhead in time is the cost of input number going from n to zero, which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().numberOfSteps( num=14 )
        self.assertEqual(result, 6)

    
    def test_case_2( self ):

        result = Solution().numberOfSteps( num=8 )
        self.assertEqual(result, 4)

    
    def test_case_3( self ):

        result = Solution().numberOfSteps( num=123 )
        self.assertEqual(result, 12)



if __name__ == '__main__':

    unittest.main()