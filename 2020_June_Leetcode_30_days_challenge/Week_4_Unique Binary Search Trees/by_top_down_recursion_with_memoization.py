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


# Let BST( n ) denotes the number of unique binary search trees with n nodes
#
# Recurrence for BST( n ) is described as following
# 
## Base case:
#
# BST( 0 ) = 1 for empty tree
# BST( 1 ) = 1 for tree with one node only
#
#
## Inductive step:
#
# For binary search tree with n nodes:
# BST( n ) 
# = 1 node as root, make left subtrees and right subtrees with n-1 nodes 
# = (Left with 0 node, Right with n-1 node) + (Left with 1 node, Right with n-2 node) + ... + (Left with n-1 node, Right with 0 node)
# = BST(0)*BST(n-1) + BST(1)*BST(n-2) + ... BST(n-1)*BST(0)
# 
# BST( n ) = BST(0)*BST(n-1) + BST(1)*BST(n-2) + ... BST(n-1)*BST(0)
            
            
            
# Let BST( n ) denotes the number of unique binary search trees with n nodes
#
# Recurrence for BST( n ) is described as following
# 
## Base case:
#
# BST( 0 ) = 1 for empty tree
# BST( 1 ) = 1 for tree with one node only


## Inductive step:
#
# For binary search tree with n nodes:
# BST( n ) 
# = 1 node as root, make left subtrees and right subtrees with n-1 nodes 
# = (Left with 0 node, Right with n-1 node) + (Left with 1 node, Right with n-2 node) + ... + (Left with n-1 node, Right with 0 node)
# = BST(0)*BST(n-1) + BST(1)*BST(n-2) + ... BST(n-1)*BST(0)
# 
# BST( n ) = BST(0)*BST(n-1) + BST(1)*BST(n-2) + ... BST(n-1)*BST(0)
            
            
            
class Solution:
        
    def __init__(self):    
        
        self.num_of_tree_table = dict()
        
        # base case:
        
        # empty tree
        self.num_of_tree_table[0] = 1
        
        # binary search tree with one node only
        self.num_of_tree_table[1] = 1
        
        
        
    def numTrees(self, n: int) -> int:
        
        if n in self.num_of_tree_table:
            return self.num_of_tree_table[n]
        
        else:
            
            num_of_unique_bst = 0
            
            for nodes_of_left_subtree in range(0, n):
                
                nodes_of_right_subtree = (n-1) - nodes_of_left_subtree
                
                num_of_unique_bst += self.numTrees( nodes_of_left_subtree ) * self.numTrees( nodes_of_right_subtree )
            
            
            # update num_of_tree memorization table
            self.num_of_tree_table[ n ] = num_of_unique_bst
            
           
        
        return num_of_unique_bst



# n : the value of input parameter

## Time Complexity: O( 3^n )
#
# The overhead in time is the cost of catalan number computation, which is of O( 3^n )

## Space Complexity: O( n )
#
# The overhead in space is the storage of num_of_tree_table, which is of O( n )


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
    