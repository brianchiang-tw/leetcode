'''

Description:

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        visit_queue = deque([(root, 1)])

        while len(visit_queue) != 0:
            # BFS Traversal

            next_visit, cur_depth =visit_queue.popleft()

            if next_visit is None:
                # empty node or empty tree
                continue
            
            if next_visit.left is None and next_visit.right is None:
                # reach a leaf node
                # get the minimal depth of binary tree, early return
                return cur_depth

            #append left and right child into visit_queue, increase current depth by 1
            visit_queue.append( (next_visit.left, cur_depth+1) )
            visit_queue.append( (next_visit.right, cur_depth + 1) )

        # depth 0 for empty-tree
        return 0



# N : the number of nodes in binary tree with given root

## Time Complexity: O( N )
#
# The overhead in time is the iterations over while loop with BFS traversal
# Best case would be O( 1 )[empty tree], but average case and worst case[right-skew tree] still takes O( N )


## Space Complexity: O( N )
#
# The overhead in space is the booking variable over while loop with BFS traversal
# Best case would be O( 1 )[empty tree], but average case and worst case[right-skew tree] still takes O( N )


def test_bench():

    # 1st test-case
    '''
    
    Example:

    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    return its minimum depth = 2.
    
    '''

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # expected output:
    '''
    2   
    '''
    print( Solution().minDepth(root) )



    # 2nd test-case
    # empty tree
    root = None

    # expected output:
    '''
    0   
    '''
    print( Solution().minDepth(root) )



    # 3rd test-case
    # right-skew tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    # expected output:
    '''
    3   
    '''
    print( Solution().minDepth(root) )



if __name__ == '__main__':

    test_bench()