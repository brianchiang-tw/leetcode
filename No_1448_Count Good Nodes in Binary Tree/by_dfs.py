'''

Description:

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.



Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.



Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper( node: TreeNode, ancestor_max: int) -> int:
            
			# update ancestor max for child node
            ancestor_max_for_child = max( ancestor_max, node.val )
			
			# visit whole tree in DFS
            left_good_count = helper( node.left, ancestor_max_for_child ) if node.left else 0
            right_good_count = helper( node.right, ancestor_max_for_child ) if node.right else 0

            return left_good_count + right_good_count + ( node.val >= ancestor_max )
        # -------------------------------------------
        return helper( root, root.val )



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).


def test_bench():

    root = TreeNode( 3 )

    root.left = TreeNode( 1 )
    root.right = TreeNode( 4 )

    root.left.left = TreeNode( 3 )
    root.right.left = TreeNode( 1 )
    root.right.right = TreeNode( 5 )

    # expected output:
    '''
    4
    '''

    print( Solution().goodNodes( root ) )



if __name__ == '__main__':

    test_bench()