# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    

    def sumNumbers(self, node: TreeNode, tree_num = 0) -> int:

        if not node:
            # empty tree or empty node
            return 0
        
        else:
            # update tree_num with current node
            tree_num = 10 * tree_num + node.val

            if not node.left and not node.right:
                # leaf is reached, return tree_num
                return tree_num

            else:
                # DFS down to next level
                return self.sumNumbers( node.left, tree_num) + self.sumNumbers( node.right, tree_num) 



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal in binary tree, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).



def test_bench():

    ## test case_#1
    root_1 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_1.right = TreeNode(3)

    # expected output:
    '''
    25
    '''

    print( Solution().sumNumbers( root_1 ) )


    ## test case_#2
    root_2 = TreeNode( 4 )
    root_2.left = TreeNode( 9 )
    root_2.right = TreeNode( 0 )

    root_2.left.left = TreeNode(5)
    root_2.left.right = TreeNode(1)

    # expected output:
    '''
    1026
    '''
    print( Solution().sumNumbers( root_2 ) )


if __name__ == '__main__':

    test_bench()    