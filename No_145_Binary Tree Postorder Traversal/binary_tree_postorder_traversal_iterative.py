'''

Description:

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        traversal_path = []
        stack_postorder = [ (root, "init") ]

        while stack_postorder:

            current, label = stack_postorder.pop()

            if current and label != "c":

                # DFS with postorder
                # left child, right child, current node

                # Stack is of Last In First Out,
                # thus push in reverse of postorder

                stack_postorder.append( (current, "c") )
                stack_postorder.append( (current.right, "r") )
                stack_postorder.append( (current.left, "l") )
            
            elif current and label == "c":

                traversal_path.append( current.val )


        return traversal_path



# N : number of nodes in binary tree

## Time Complexity: O( N )
#
# The overhead in time is the while loop, iterating every node with postorder.
# Each single visit on one node takes O( 1 ), total n nodes takes O( N ).

## Space Complexity: O( N )
#
# The overhead in space is to maintain stack_postorder.
# The worst case is O( N ) of left-skew tree or right-skew tree.



def test_bench():

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    path_of_postorder = Solution().postorderTraversal( root )

    # expected output:
    '''
    [3, 2, 1]
    '''

    print( path_of_postorder )

    return 



if __name__ == '__main__':

    test_bench()