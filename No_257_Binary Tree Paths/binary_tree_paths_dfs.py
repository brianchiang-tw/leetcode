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
    
    def leaf_path(self, root: TreeNode, path, bag_of_path) ->List[int]:
        
        if root is None:
            return None
        
        else:
            
            cur_path = path[::]
            cur_path.append( str(root.val) )
            
            left = self.leaf_path( root.left, cur_path[::], bag_of_path)
            right = self.leaf_path( root.right, cur_path[::], bag_of_path)

            if left is None and right is None:
                # catch one root-to-leaf path
                bag_of_path.append( cur_path )
                
            return bag_of_path
    
    
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        list_of_leaf_path = self.leaf_path( root, [], [] )
        
        if list_of_leaf_path is None:
                # empty tree
            return []
    
        else:
                # non-empty tree
            list_of_str_path = [ "->".join(p) for p in list_of_leaf_path ]
            return list_of_str_path



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