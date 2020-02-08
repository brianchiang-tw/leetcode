'''

Description:

Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

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
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        # Initialization:
        # prev level as empty list
        # traversal queue as root node
        prev_level, traversal_queue = [],  [ root ]
        
        # Level-order-traversal
        while traversal_queue:
            
            # update previous level as current traversal queue 
            # update current traversal queue as next level queue
            prev_level, traversal_queue = traversal_queue, [ leaf for node in traversal_queue for leaf in (node.left, node.right) if leaf ]
        
        
        # When the level-order-traversal is completed,
        # prev_level contains those nodes in deepest level
        return sum( node.val for node in prev_level if node )
                


# n : the number of nodes

## Time Complexity: O(n)
#
# The overhead in time is the cost of level-order traversal, which is of O( n )

## Space Complexity: O(n)
#
# The overhead in space is the storage for traversal_queue, which is of O( n )



def test_bench():

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    
    node_4.left = node_7

    node_2.left = node_4
    node_2.right = node_5

    node_6.right = node_8
    node_3.right = node_6
    
    node_1.left = node_2
    node_1.right = node_3

    root = node_1

    print( Solution().deepestLeavesSum(root) )

    return



if __name__ == '__main__':

    test_bench()                