'''

Description:

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

'''



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # -----------------------------------
        
        # key: (m, n) size of grid
        # value: total path count from source to destinaion
        memo = {}
        
        def path_count(m, n):
            
            if (m, n) in memo:
                
                # look-up in memo
                return memo[(m, n)]
            
            if m == 0 or n == 0:
                
                # base case
                memo[(m, n)] = 0
                return 0
            
            elif m == 1 and n == 1:
                
                # base case
                memo[(m, n)] = 1
                return 1

            # general case
            memo[(m, n)] = path_count(m-1, n) + path_count(m, n-1)
            return memo[(m, n)]
    
        # -----------------------------------
        return path_count(m, n)



# m, n : dimension of rows and columns

## Time Complexity: O( m * n )
#
# The overhead in time is the recursion from (m, n) down to (0, 0), which is of O( m * n)

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for memoization, which is of O( m * n)


import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_case_1( self ):

        result = Solution().uniquePaths( m=3, n=2)
        self.assertEqual(result, 3)


    def test_case_2( self ):

        result = Solution().uniquePaths( m=7, n=3)
        self.assertEqual(result, 28)

    
    def test_case_3( self ):

        result = Solution().uniquePaths( m=6, n=8)
        self.assertEqual(result, 792)
    

if __name__ == '__main__':

    unittest.main()