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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        cache = { 0 : 1}
        
        def helper( node: TreeNode, target: int, cur_sum: int, table: dict):
            
            if node:
                cur_sum = cur_sum + node.val

                candidate = cur_sum - target

                cur_method_count = table.get(candidate, 0 )
                
                table[cur_sum] = table.get( cur_sum, 0) + 1

                left_method_count = helper( node.left, target, cur_sum, table )
                right_method_count = helper( node.right, target, cur_sum, table )

                table[cur_sum] -= 1

                return left_method_count + cur_method_count + right_method_count
            else:
                # empty node has no chance to create path sum, which meets target
                return 0
        # --------------------
        
        return helper( root, sum, 0, cache)



# n : the number of node in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).


def test_bench():

    root = TreeNode( 10 )
    
    root.left = TreeNode( 5 )
    root.right = TreeNode( -3 )

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)

    root.right.right = TreeNode(11)

    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)

    print( Solution().pathSum( root = root, sum = 8) )


    return



if __name__ == '__main__':

    test_bench()