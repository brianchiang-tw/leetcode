'''

Description:

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def helper( node: TreeNode, parent: int, grandparent: int):
        
            if not node:
                # base case:
                # empty node or empty tree
                return 0
            
            summation = 0
            
            # update summation if grandparent is of even value
            if grandparent%2 == 0:    
                 summation += node.val
            
            
            # update grandparent as current parent
            # update parent as current node's value
            # DFS down to next level
            summation += helper( node.left, node.val, parent)
            summation += helper( node.right, node.val, parent)
                
            return summation
        
        #--------------------------------------------------------
        
        return helper( root, -1, -1)



# n : the number of nodes in binary tree
# h : the height of binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of pre-order DFS traversal, which is if O( n ).

## Space Complexity: O( h )
#
# The overhead in space is the storage for recursion call stack, which is of O( h ).



def test_bench():

    root = TreeNode(6)

    root.left = TreeNode(7)
    root.right = TreeNode(8)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)

    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)

    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)

    # expected output:
    '''
    18
    '''

    print( Solution().sumEvenGrandparent(root) )

    return 



if __name__ == '__main__':
    
    test_bench()