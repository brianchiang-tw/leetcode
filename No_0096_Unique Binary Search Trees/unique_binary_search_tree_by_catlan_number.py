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
        # = Catlan number of n
        # = C(2n, n) / ( n + 1)
        
        num_of_unique_bst = ( self.combination_n_m( 2*n, n) ) // (n+1)

        return num_of_unique_bst


# N : the value of input n

## Time Complexity : O( N )
#
# Though it seems to be O( 1 ) at first glimpse, but it takes O( N ) actually, 
# due to the computation of C(2n, n), grows in order of O( N )

## Space Complexity : O( 1 )
#
# The overhead in space is the variable for mathatical operation with fixed size.


def test_bench():

    test_data = [1,2,3,4,5]

    # expected output:
    '''
    1
    2
    5
    14
    42
    '''


    for n in test_data:

        print( Solution().numTrees(n) )

    return



if __name__ == '__main__':

    test_bench()