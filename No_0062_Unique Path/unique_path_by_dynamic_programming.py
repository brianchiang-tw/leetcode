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
        
        rows, cols = m, n
        
        path_dp = [ [ 1 for j in range(cols)] for i in range(rows) ]
        
        
        # Dynamic Programming relation:
        
        # Base case:
        # DP(0, j) = 1 , only reachable from one step left
        # DP(i, 0) = 1 , only reachable from one step up
        
        # General case:
        # DP(i,j) = number of path reach to (i, j)
        #         = number of path reach to one step left + number of path reach to one step up
        #         = number of path reach to (i, j-1) + number of path to (i-1, j)
        #         = DP(i, j-1) + DP(i-1, j)
        
        
        
        for i in range(1, rows):
            for j in range(1, cols):
                
                path_dp[i][j] = path_dp[i][j-1] + path_dp[i-1][j]
        
        
        # Destination coordination = (rows-1, cols-1)
        return path_dp[rows-1][cols-1]



# m, n : dimension of rows and columns

## Time Complexity: O( m * n )
#
# The overhead in time is the nested for loops iterating on (i, j), which is of O( m * n)

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for table path_dp, which is of O( m * n)



def test_bench():

    test_data = [(3,2), (7,3), (6,8)]

    for m, n in test_data:

        print( Solution().uniquePaths( m, n) )
    
    return



if __name__ == '__main__':

    test_bench()