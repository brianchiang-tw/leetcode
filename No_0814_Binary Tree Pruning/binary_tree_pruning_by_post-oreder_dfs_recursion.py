'''

Description:

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:

Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]



Note:

The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def prune_helper( self, node: TreeNode ):
        '''
        Input: one node as root node of binary tree
        Output: Repeat remove all leaf node whose value is 0 until all leaf nodes is non-zero
        '''

        if not node:
            # base case:
            # empty node or empty tree
            return True

        
        # pre-order DFS down to next level
        left_removal = self.prune_helper( node.left )
        right_removal = self.prune_helper( node.right )

        
        if left_removal and right_removal and node.val == 0:
            # update node as prune target by return True
            return True

        if left_removal:
            # prune left leaf node
            node.left = None

        if right_removal:
            # prune right leaf node
            node.right = None

        # node is either a non-leaf node, or a leaf node with 1
        return False

    
    
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        
        if self.prune_helper(root):
            # root is empty node naturally, or pruned finally.
            return None
        else:
            # root still exists eventually
            return root



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of post-order DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the recusion call stack, which is of O( n )



def inorder_print( node :TreeNode):

    if node:

        inorder_print( node.left )
        print(f'{node.val} ', end = '')
        inorder_print( node.right )


def test_bench():

    root = TreeNode( 1 )

    root.left = TreeNode( 0 )
    root.right = TreeNode( 1 )
    
    root.left.left = TreeNode( 0 )
    root.left.right = TreeNode( 0 )
    root.right.left = TreeNode( 0 )
    root.right.right = TreeNode( 1 )

    Solution().pruneTree( root )

    # expected output:
    '''
    1 1 1
    '''
    inorder_print( root )

    return



if __name__ == '__main__':

    test_bench()
    