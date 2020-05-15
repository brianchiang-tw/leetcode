# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def clone_with_offset(self, node: TreeNode, offset):
        
        if not node:
            return None
        
        else:
            
            # Clone whole tree with constant value offset
            root_node = TreeNode( node.val + offset )
            root_node.left = self.clone_with_offset( node.left, offset )
            root_node.right = self.clone_with_offset( node.right, offset )
            
            return root_node
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        
        if n == 0:
            # Quick response for empty tree
            return []
        
        # dynamic programming table
        bst_dp_table = [ None for i in range(n+1) ]
        
        # base case: 
        bst_dp_table[0] = [None]
        
        
        # bottom-up. build bst with k nodes, k from 1 to n
        for number_of_nodes in range(1, n+1):
            
            bst_dp_table[number_of_nodes] = []
            
            # for root node of bst:     1 node                            
            # for left-subtree of bst : (number_of_nodes_on_left) nodes     
            # for right-subtrr of bst : (k-1-number_of_nodes_on_left) nodes 
            for number_of_nodes_on_left in range(0, number_of_nodes):
                
                for left_subtree in bst_dp_table[number_of_nodes_on_left]:
                    
                    number_of_nodes_on_right = number_of_nodes-1-number_of_nodes_on_left
                    
                    for right_subtree in bst_dp_table[number_of_nodes_on_right]:
                        
                        # construct one unique nst
                        root_of_bst = TreeNode( number_of_nodes_on_left+1 )
                        root_of_bst.left = left_subtree
                        root_of_bst.right = self.clone_with_offset(right_subtree, number_of_nodes_on_left+1)
                        
                        # update dynamic programming table
                        bst_dp_table[number_of_nodes].append( root_of_bst )
            
        return bst_dp_table[n]



# N : the value of input n

## Time Complexity : O( 4^N )
#
# Due to the groth rate of Catalan(n), it is  of O( 4^N )

## Space Complexity : O( 4^N )
#
# The overhead in space is the storage for look-up table, bst_dp_table, which is of O( 4^N ).