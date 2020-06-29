'''

Description:

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5

Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''


from math import factorial
class Solution:
    
    def combination_n_m(self, n: int, m:int)->int:

        if m == 0 or n == m:
            return 1
        else:
            return factorial(n) // ( factorial( m ) * factorial( n-m ) )
    
    
    def numTrees(self, n: int) -> int:
        
        # Number of structurally unique bst wieth n nodes 
        # = Catalan number of n
        # = C(2n, n) / ( n + 1)
        
        num_of_unique_bst = ( self.combination_n_m( 2*n, n) ) // (n+1)

        return num_of_unique_bst



# n : the value of input parameter

## Time Complexity: O( 3^n )
#
# The overhead in time is the cost of catalan number computation, which is of O( 3^n )

## Space Complexity: O( 1 )
#
# The overhead in space is the cost of temporary variable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().numTrees(0)
        self.assertEqual( result, 1)



    def test_case_2( self ):

        result = Solution().numTrees(1)
        self.assertEqual( result, 1)



    def test_case_3( self ):
    
        result = Solution().numTrees(2)
        self.assertEqual( result, 2)



    def test_case_4( self ):
    
        result = Solution().numTrees(3)
        self.assertEqual( result, 5)




    def test_case_5( self ):
    
        result = Solution().numTrees(10)
        self.assertEqual( result, 16796)


if __name__ == '__main__':

    unittest.main()
    