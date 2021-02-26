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


'''
Math analysis:

Case_#1:
num is 0. No extra step is taken, directly return 0.

Case_#2:
num is non-zero.
Take num into binary form.

The reduce procedure includes:
a. Drop 0 on the tail, when last bit is 0 ( for even number, except for 0 )
b. Flip 1 to 0 on the tail, when last bit is 1 ( for odd number )

Example:

10 in decimal = 1010 in binary

1010 -> 101 ( Drop 0 on the tail)
101 -> 100 ( Flip 1 to 0 on the tail )
100 -> 10 ( Drop 0 on the tail )
10 -> 1 ( Drop 0 on the tail )
1 -> 0 ( Flip 1 to 0 on the tail )
0 ( Accomplished, it is reduced to 0 already, no need to drop this time)

Total steps:
= length of bitstring - 1 + count of 1 in bitsring
= length of bitstring + count of 1 in bitsring - 1
= 4 + 2 - 1
= 5
'''

class Solution:
    
    def numberOfSteps (self, num: int) -> int:
        
        if not num:
            return 0
            
        else:
            bit_string = bin(num)[2:]
            return len(bit_string) + bit_string.count('1') - 1 


## Time Complexity: O( log n )
#
# The overhead in time is the cost of bit string generation of n, which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 )


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