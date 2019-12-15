# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List

class Solution:
    
    def __init__(self):
        self.traversal_path = []
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack_inorder = [ (root, "i") ]

        while stack_inorder:

            current, label = stack_inorder.pop()

            # DFS with inorder
            # left child, current, right child
            if current and label != "c":

                # Stack if Last-in First Out, so push in reverse of inorder.
                stack_inorder.append( (current.right, "r" ) )
                stack_inorder.append( (current, "c" ) )
                stack_inorder.append( (current.left, "l" ) )

            elif current and label == "c":
                self.traversal_path.append( current.val )

        return self.traversal_path

# N : number of node in binary tree with given root

## Time Complexity:
#
# Inorder traversal visits each node once, every single visit costs O(1).
# There are n nodes in binary tree, thus totally it takes O( n ).

## Space Complexity:
#
# The overhead in time is to maintain stack for inorder traversal,
# It is O( n ) at most.

def test_bench():

    root = TreeNode(1)

    root.right = TreeNode(2)

    root.right.left = TreeNode(3)

    in_order_traversal = Solution().inorderTraversal(root)

    # expected output:
    '''
    [1, 3, 2]
    '''
    print( in_order_traversal )


    return



if __name__ == '__main__':

    test_bench()