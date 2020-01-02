'''

Description:

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

'''



from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        if root is None: 
            return []

        if root.left is None and root.right is None:
            return [ str(root.val) ]

        all_root_to_leaf_path = \
            [ str(root.val) + '->' + node for node in self.binaryTreePaths(root.left)  ] + \
            [ str(root.val) + '->' + node for node in self.binaryTreePaths(root.right) ]

        return all_root_to_leaf_path



# n : the number of nodes in given input binary tree

## Time Complexity: O( n )
#
# The overhead in time is to traverse each node in DFS, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is to maintain path and bag-of-path to track root-to-leaf path.
# In addition, the the number of root-to-leaf paths is of O( n )



def test_bench():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)

    # expected output:
    '''
    ['1->2->5', '1->3']
    '''
    print( Solution().binaryTreePaths(root) )

    return



if __name__ == '__main__':

    test_bench()