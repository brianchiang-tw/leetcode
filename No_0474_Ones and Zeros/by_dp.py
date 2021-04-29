'''

Description:

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.



Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100

'''

from typing import List

class Solution:

    def findMaxForm(self, strs: List[str], m:int, n:int)-> int:

        # dynamic programming table fpr subset making up to m zeros and n ones
        dp = [ [ 0 for _ in range(m+1)] for _ in range(n+1) ]

        # scan each string
        for string in str:

            # total zeros and ones of current string
            zeros = string.count('0')
            ones = len(string) - zeros

            # check for each subcase
            for N in range(n, ones-1, -1):
                for M in range(m, zeros-1, -1):

                    # maximize subset size from growing on smaller cases with string
                    dp[N][M] = max(1 + dp[N-ones][M-zeros], dp[N][M])

        
        return dp[n][m]


# s: the lnegth of strs
# m, n : input value of variable m, n

## Time complexity: O( s * m * n )
#
# The overhead in time is the cost of nested iteration, which is of O( s * m * n)

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for dynamic programming table, which is of O( m * n )


import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().findMaxForm
        return

    def test_case_1( self ):

        result = self.solver( strs = ["10","0001","111001","1","0"], m = 5, n = 3 )
        self.assertEqual(result, 4)

    def test_case_2( self ):

        result = self.solver( strs = ["10","0","1"], m = 1, n = 1 )
        self.assertEqual(result, 2)

if __name__ == '__main__':

    unittest.main()        