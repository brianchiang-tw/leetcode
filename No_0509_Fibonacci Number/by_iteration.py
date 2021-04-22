'''

Description:

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.

'''


class Solution:
    def fib(self, n: int) -> int:
        
        ## base cases
        if n == 0 or n == 1:
            return n
        
        ## general cases
        prev_2, prev_1 = 0, 1
        
        for _ in range(1,n):
            
            cur = prev_2 + prev_1
            prev_2, prev_1 = prev_1, cur
            
        return cur


# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Sapce Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary varaible, which is of O( 1 )

import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().fib
        return

    def test_case_1( self ):

        result = self.solver(0)
        self.assertEqual(result, 0)

    def test_case_2( self ):

        result = self.solver(1)
        self.assertEqual(result, 1)

    def test_case_3( self ):

        result = self.solver(2)
        self.assertEqual(result, 1)

    def test_case_4( self ):

        result = self.solver(3)
        self.assertEqual(result, 2)                

    def test_case_5( self ):

        result = self.solver(4)
        self.assertEqual(result, 3)

    def test_case_6( self ):

        result = self.solver(5)
        self.assertEqual(result, 5)

    def test_case_7( self ):

        result = self.solver(10)
        self.assertEqual(result, 55)

    def test_case_8( self ):

        result = self.solver(30)
        self.assertEqual(result, 832040)

if __name__ == '__main__':

    unittest.main()        