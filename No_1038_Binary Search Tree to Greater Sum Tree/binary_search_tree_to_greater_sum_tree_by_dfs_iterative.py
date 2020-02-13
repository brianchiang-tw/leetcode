'''

Description:

Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 

Note:

The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        accumulation = 0
        traversal_stack = [ (root, 'init') ]
        
        while traversal_stack:
            
            cur_node, cur_state = traversal_stack.pop()
            
            if cur_node:
                
                if cur_state == 'cur':
                    
                    accumulation += cur_node.val
                    cur_node.val = accumulation

                else:

                    traversal_stack.append( (cur_node.left, 'left') )
                    traversal_stack.append( (cur_node, 'cur') )
                    traversal_stack.append( (cur_node.right, 'right') )

        return root



# n : number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of reversed in-order DFS traversal, which is of O( n ).


## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal stack, which is of O( n )
        


def print_inorder( node: TreeNode):

    if node:

        print_inorder( node.left )
        print(f'{node.val} ', end = '')
        print_inorder( node.right )

    return

def test_bench():

    
    node_0 = TreeNode( 0 )
    node_1 = TreeNode( 1 )
    node_2 = TreeNode( 2 )
    node_3 = TreeNode( 3 )
    node_4 = TreeNode( 4 )
    node_5 = TreeNode( 5 )
    node_6 = TreeNode( 6 )
    node_7 = TreeNode( 7 )
    node_8 = TreeNode( 8 )

    root = node_4
    root.left = node_1
    root.right = node_6

    node_1.left = node_0
    node_1.right = node_2

    node_6.left = node_5
    node_6.right = node_7

    node_2.right = node_3
    node_7.right = node_8

    # before:
    # expected output:
    '''
    0 1 2 3 4 5 6 7 8
    '''    
    print_inorder( root )

    Solution().bstToGst( root )
    print("\n")

    # after:
    # expected output:
    '''
    36 36 35 33 30 26 21 15 8
    '''
    print_inorder( root )

    return 



if __name__ == '__main__':

    test_bench()