'''

Description:

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        sum_counter_dict = { 0 : 1}
        
        counter_valid_path = 0
        
        def helper( node: TreeNode, target: int, cur_sum: int, table: dict):
            
            if not node:
                # empty node or empty tree
                return
            
            
            cur_sum += node.val
            
            # compute candidate sum
            candidate_sum = cur_sum - target
            
            # update counter of valid path if candidate sum exist in table
            nonlocal counter_valid_path
            counter_valid_path += table.get(candidate_sum, 0)
            
            table[cur_sum] = table.get(cur_sum, 0) + 1
            
            # DFS down to next level
            helper( node.left, target, cur_sum, table)
            helper( node.right, target, cur_sum, table)
            
            # This subtree DFS is completed, decrease the method count of cur_sum by 1
            table[cur_sum] -= 1
            
        # ----------------------------------------
        helper( root, sum, 0, sum_counter_dict)
        return counter_valid_path



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of dfs, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, as well as dictionary, which are of O( n ).


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        root = TreeNode(10)

        root.left = TreeNode(5)
        root.right = TreeNode(-3)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(11)

        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right.right = TreeNode(1)

        result = Solution().pathSum(root=root)
        self.assertEqual(result, 3)


if __name__ == '__main__':

    unittest.main()