'''

Description:

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        accumulation = 0
        
        def converter( node: TreeNode) -> TreeNode:
            
            if not node:
                # Base case (also known as stop condition)
                # empty node or empty tree
                return None
            
            else:
                # General case:
                # DFS down to next level with reversed in-order traversal
                
                
                if node.right:
                    converter( node.right )
                
                # update accumulation and assign to current node
                nonlocal accumulation
                accumulation += node.val
                node.val = accumulation
                
                if node.left:
                    converter( node.left )
                
                return node
            
        # ----------------------------------
        
        return converter(root)



# n : number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of reversed in-order DFS traversal, which is of O( n ).


## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal stack, which is of O( n )
        


def print_inorder( node: TreeNode):

    if node:

        print_inorder( node.left )
        print(f'{node.val} ', end = '')
        print_inorder( node.right )

    return

def test_bench():

    
    node_0 = TreeNode( 0 )
    node_1 = TreeNode( 1 )
    node_2 = TreeNode( 2 )
    node_3 = TreeNode( 3 )
    node_4 = TreeNode( 4 )
    node_5 = TreeNode( 5 )
    node_6 = TreeNode( 6 )
    node_7 = TreeNode( 7 )
    node_8 = TreeNode( 8 )

    root = node_4
    root.left = node_1
    root.right = node_6

    node_1.left = node_0
    node_1.right = node_2

    node_6.left = node_5
    node_6.right = node_7

    node_2.right = node_3
    node_7.right = node_8

    # before:
    # expected output:
    '''
    0 1 2 3 4 5 6 7 8
    '''    
    print_inorder( root )

    Solution().convertBST( root )
    print("\n")

    # after:
    # expected output:
    '''
    36 36 35 33 30 26 21 15 8
    '''
    print_inorder( root )

    return 



if __name__ == '__main__':

    test_bench()