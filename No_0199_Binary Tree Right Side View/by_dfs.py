'''

Description:

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List
from collections import defaultdict

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
			# Quick response for empty tree
            return []
        
        # key: depth
		# value: value of right-most node
        self.side_view_dict = defaultdict( int )
        self.max_depth = 0
        
        def helper( node: TreeNode, depth: int):
            
            if node:
                
                if self.side_view_dict.get(depth, None) == None:
                    self.side_view_dict[depth] = node.val
                
                self.max_depth = max( self.max_depth, depth)
                
                # Let right sub-tree go before left sub-tree in order to get right side view
                helper( node.right, depth+1 )
                helper( node.left, depth+1 )
        
        # ----------------------------------------
        helper( node = root, depth = 0 )
        return [ self.side_view_dict[depth] for depth in range(0, self.max_depth+1) ]



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the stroage for recursion stack, which is of O( n ).


def test_bench():

    root = TreeNode( 1 )

    root.left = TreeNode( 2 )
    root.right = TreeNode( 3 )

    root.left.right = TreeNode( 5 )
    root.right.right = TreeNode( 4 )

    # expected output:
    '''
    [1, 3, 4]
    '''

    print( Solution().rightSideView( root ) )



if __name__ == '__main__':

    test_bench()