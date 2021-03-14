'''

Description:

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
 

Example 1:


Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]



Example 2:


Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
The depth of the tree is in the range [1, 104].
-100 <= Node.val <= 100
-105 <= val <= 105
1 <= depth <= the depth of tree + 1

'''

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        if not root:

            # bcase case: empty tree
            return None

        elif d == 1:

            # base case: add one row above original root
            return TreeNode(v, left=root, right=None)

        elif d == 2:

            # base case: add one row below original root
            root.left = TreeNode(v, left=root.left, right=None)
            root.right = TreeNode(v, left=None, right=root.right)

            return root
        else:

            # general case: depth >= 3
            # do it in DFS with common pattern
            root.left = self.addOneRow(root.left, v, d-1)
            root.right = self.addOneRow(root.right, v, d-1)

            return root



# n : the number of nodes

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion, which is of O( n )


def levelOrder( root: TreeNode) -> List[List[int]]:
        
        
        if not root:
            # Quick response for empty tree
            return []
        
        traversal_queue, result = [root], []
        
        # level order traversal
        while traversal_queue:
            
            # add current level into result
            result.append([node.val for node in traversal_queue])
            
            # record current level child nodes
            child_pair = [(node.left, node.right) for node in traversal_queue]
            
            # update traversal queue with next level nodes
            traversal_queue = [ child for pair in child_pair for child in pair if child ]
            
        return result

# ----------------------------------------

import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        root = TreeNode(4)

        root.left = TreeNode(2)
        root.right = TreeNode(6)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)

        root.right.left = TreeNode(5)

        root = Solution().addOneRow(root, v=1, d=2)
        result = levelOrder(root)
        self.assertEqual(result, [[4], [1,1], [2,6], [3,1,5]])


    def test_case_2(self):

        root = TreeNode(4)

        root.left = TreeNode(2)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)

        root = Solution().addOneRow(root, v=1, d=3)
        result = levelOrder(root)
        self.assertEqual(result, [[4], [2], [1,1], [3,1]])


if __name__ == '__main__':

    unittest.main()