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
            
            
            
class Solution:
        

    
    def numTrees(self, n: int) -> int:
        
        num_of_bst_dp = [ 0 for i in range(n+1) ]


        
        ## base case:
        # empty tree
        num_of_bst_dp[ 0 ] = 1
        
        # bst with one node only
        num_of_bst_dp[ 1 ] = 1 
        
        #print(num_of_bst_dp)
        
        for k in range(2, n+1):
            
            num_of_unique_bst = 0

            for nodes_of_left_subtree in range(0, k):

                nodes_of_right_subtree = (k-1) - nodes_of_left_subtree
                
                num_of_unique_bst += num_of_bst_dp[nodes_of_left_subtree]*num_of_bst_dp[nodes_of_right_subtree]
            
            # update dynamic programming table for number of binary search tree
            num_of_bst_dp[ k ] = num_of_unique_bst
           
        
        return num_of_bst_dp[ n ]



# N : the value of input n

## Time Complexity : O( 4^N )
#
# Due to the groth rate of Catlan(N), it is  of O( 4^N )

## Space Complexity : O( 4^N )
#
# The overhead in space is the storage for dictionary, num_of_tree_table, which is of O( 4^N ).


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