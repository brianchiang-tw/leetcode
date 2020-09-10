'''

Description:

You are given two images img1 and img2 both of size n x n, represented as binary, square matrices of the same size. (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

 

Example 1:

Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We slide img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3. (Shown in red)




Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1



Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0
 

Constraints:

n == a.length
n == a[i].length
n == b.length
n == b[i].length
1 <= n <= 30
a[i][j] is 0 or 1.
b[i][j] is 0 or 1.

'''


from collections import Counter

class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        
        N = len(A)
        
        
        # position of 1 in matrix A
        pos_of_1_in_A = [(xi, yi) for xi in range(N) for yi in range(N) if A[xi][yi]]
        
        # position of 1 in matrix B
        pos_of_1_in_B = [(xi, yi) for xi in range(N) for yi in range(N) if B[xi][yi]]
        
        offset_vector_counting = Counter([(x1 - x2, y1 - y2) for (x1, y1) in pos_of_1_in_A for (x2, y2) in pos_of_1_in_B ])
        
        # the highest counting value is the largest overlap with most 1s
        return max(offset_vector_counting.values() or [0])


# n : the maximum side length of A and B

## Time Complexity: O( n^4 )
#
# The overhead in time is the cost of nested loops in dictionary building, which is of O( n^4 )

## Space Complexity: O( n^4 )
#
# The overhead in space is the storage for offset_vector_counting, which is of O( n^4 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().largestOverlap(A = [[1,1,0],[0,1,0],[0,1,0]], B = [[0,0,0],[0,1,1],[0,0,1]] )
        self.assertEqual(result, 3)


    def test_case_2( self ):

        result = Solution().largestOverlap(A = [[1]], B = [[1]] )
        self.assertEqual(result, 1)


    def test_case_3( self ):

        result = Solution().largestOverlap(A = [[0]], B = [[0]] )
        self.assertEqual(result, 0)


if __name__ == '__main__':

    unittest.main()

