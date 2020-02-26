'''

Description:

Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
 

Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Explanation: 
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".



Example 2:

Input: root = [1,2,3,4]
Output: [4]



Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]
 

Constraints:

The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def helper( node: TreeNode, depth: int ) -> TreeNode:
            
            if not node:
                # Base case aka stop condition
                # current node is leaf node
                return (None, depth)
            
            else:
                
                left_lca, left_depth = helper( node.left, depth+1 )
                right_lca, right_depth = helper( node.right, depth+1 )
                
                if left_depth < right_depth : 
                    
                    # right sub-tree is deeper
                    return (right_lca, right_depth )
                
                elif left_depth >  right_depth: 
                    
                    # left sub-tree is deeper
                    return (left_lca, left_depth )
                
                else:
                    
                    # both sub-tree is of the same depth
                    # current is ancestor of leave
                    # current depth = left_depth = right_depth
                    return ( node, left_depth )
                
        # ----------------------
        return helper( node = root, depth = 0 )[0]


# n : the number of node in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of post-order DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


def test_bench():

    ## Test case_#1
    root_1 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_1.right = TreeNode(3)

    # expected output:
    '''
    1
    '''
    print( Solution().lcaDeepestLeaves(root_1).val )



    ## Test case_#2
    root_2 = TreeNode(1)
    root_2.left = TreeNode(2)
    root_2.right = TreeNode(3)
    root_2.left.left = TreeNode(4)
    # expected output:
    '''
    4
    '''
    print( Solution().lcaDeepestLeaves(root_2).val )



    ## Test case_#3
    root_3 = TreeNode(1)
    root_3.left = TreeNode(2)
    root_3.right = TreeNode(3)
    root_3.left.left = TreeNode(4)
    root_3.left.right = TreeNode(5)
    # expected output:
    '''
    2
    '''
    print( Solution().lcaDeepestLeaves(root_3).val )

    return



if __name__ == '__main__':

    test_bench()