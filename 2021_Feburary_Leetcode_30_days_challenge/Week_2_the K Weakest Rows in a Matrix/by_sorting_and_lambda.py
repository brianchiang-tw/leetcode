'''

Description:

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].



Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
 

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.

'''


from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        h = len(mat)
        
        # build the strength list with pair
        # first item is summation of soldier
        # second item is row index
        strength = [ (sum(mat[row_idx]), row_idx )for row_idx in range(h) ]
        
        # sort by (summation of soldier, row index)
        strength.sort( key = lambda pair: (pair[0], pair[1]) )
        
        # get the first k weakest rows
        return [ strength[i][1] for i in range(k) ]



# m : the height of matrix
# n : the width of matrix

## Time Complexity: O( m * n + m log m ) 
#
# The overhead in tim is the cost of strength building and sorting

## Space Complexity: O( m )
#
# THe overhead in time is the storage for strength


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().kWeakestRows( mat=[[1,1,0,0,0],
                                            [1,1,1,1,0],
                                            [1,0,0,0,0],
                                            [1,1,0,0,0],
                                            [1,1,1,1,1]],
                                          k=3)

        self.assertEqual(result, [2, 0, 3] )


    def test_case_2( self ):

        result = Solution().kWeakestRows( mat=[[1,0,0,0],
                                            [1,1,1,1],
                                            [1,0,0,0],
                                            [1,0,0,0]], 
                                          k=2)

        self.assertEqual(result, [0, 2] )


if __name__ == '__main__':

    unittest.main()