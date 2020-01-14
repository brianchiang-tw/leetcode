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


# N : the value of input n

## Time Complexity : O( 4^N )
#
# Due to the groth rate of Catlan(N), it is  of O( 4^N )

## Space Complexity : O( n )
#
# The overhead in space is the storage for dictionary, num_of_tree_table, which is of O( n ).


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