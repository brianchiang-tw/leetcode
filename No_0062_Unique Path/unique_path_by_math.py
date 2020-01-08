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


from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows, cols = m, n
        
        # from start to destination, we need (m-1) → moves and (n-1) ↓ moves
        # Thus, the number of unique paths is the number of permutations of (m-1) → and (n-1) ↓
        #
        # Number of unique paths = ( m-1 + n-1 ) ! / (m-1)! * (n-1)!
        
        
        return factorial( m+n-2 ) // ( factorial( m-1 ) * factorial( n-1 ) )    



# m, n : dimension of rows and columns

## Time Complexity: O( m * n )
#
# The overhead in time is the factorial of ( m+n-1), which is of O( m * n )

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for pure math computation, which is of O( 1 )


def test_bench():

    test_data = [(3,2), (7,3), (6,8)]

    for m, n in test_data:

        print( Solution().uniquePaths( m, n) )
    
    return



if __name__ == '__main__':

    test_bench()