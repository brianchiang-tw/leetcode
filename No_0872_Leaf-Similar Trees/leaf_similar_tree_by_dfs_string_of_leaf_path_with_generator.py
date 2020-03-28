'''

Description:

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

Both of the given trees will have between 1 and 100 nodes.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        
        def helper( node: TreeNode):
            
            if node:
                
                yield from helper( node.left )
                
                if not node.left and not node.right:
                    yield node.val
            
                yield from helper( node.right )
        
            else:
                return
            
        #----------------------------------------------
        
        return ''.join( map(str, helper(root1) ) ) == ''.join( map(str, helper(root2) ) )






# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of in-order traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )



def test_bench():

    root_1 = TreeNode(5)
    root_1.left = TreeNode(1)
    root_1.right = TreeNode(3)

    root_2 = TreeNode(5)
    root_2.left = TreeNode(1)
    root_2.right = TreeNode(3)

    root_3 = TreeNode(5)
    root_3.left = TreeNode(1)
    root_3.right = TreeNode(6)

    # expected output:
    '''
    True
    False
    False
    '''

    print( Solution().leafSimilar( root_1, root_2 ) )
    print( Solution().leafSimilar( root_1, root_3 ) )
    print( Solution().leafSimilar( root_2, root_3 ) )



if __name__ == '__main__':

    test_bench()