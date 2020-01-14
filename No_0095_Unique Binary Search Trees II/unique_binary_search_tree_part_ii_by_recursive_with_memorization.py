'''

Description:

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

''' 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        
        # memorization table
        # key   : (lower bound of bst, upper bound of bst)
        # value : a list of bst, all nodes' value in range lower bound to upper bound.
        self.bst_dict = dict()
    
    def tree_factory(self, min_val, max_val):
        
        tree_list = []
        
        if min_val > max_val:
            # Invalid case
            tree_list.append( None )
            return tree_list
        
        if (min_val, max_val) in self.bst_dict:
            # speed-up by looking memorization table
            return self.bst_dict[(min_val, max_val)]
        
        
        # generate binary search from all possible root node value
        for root_node_value in range( min_val, max_val+1):
            
            left_sub_trees = self.tree_factory( min_val, root_node_value-1 )
            right_sub_trees = self.tree_factory( root_node_value+1, max_val )
            
            for left_subtree in left_sub_trees:
                for right_subtree in right_sub_trees:
                    
                    # construct one unique bst
                    root_node = TreeNode( root_node_value )
                    root_node.left = left_subtree
                    root_node.right = right_subtree
                    
                    tree_list.append( root_node )
        
        # update memorization table
        self.bst_dict[(min_val, max_val)] = tree_list            
        return tree_list
        
        
        
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            # Quick response for empty tree
            return []
        else:
            return self.tree_factory( min_val = 1, max_val = n )
        


# N : the value of input n

## Time Complexity : O( 4^N )
#
# Due to the groth rate of Catalan(n), it is  of O( 4^N )

## Space Complexity : O( N )
#
# The overhead in space is the storage for memorization dict, bst_dict, which is of O( N ).