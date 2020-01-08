'''

Description:

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        root_node = None
        
        if not t1:
            return t2
        
        elif not t2:
            return t1
        
        else:
            
            root_node =  TreeNode( t1.val + t2.val )
            root_node.left = self.mergeTrees( t1.left, t2.left )
            root_node.right = self.mergeTrees( t1.right, t2.right )
            
            return root_node



# n : max ( number of node of nodes in binary t1, t2 )

## Time Complexity: O( n )
#
# The overhead in time is the DFS traversal of a binary tree, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in spae is the storage for a whole new binary tree, which is of O( n )



def traverse( node: TreeNode):

    if node:

        traverse( node.left )

        print( node.val, end = ' ')

        traverse( node.right )


def test_bench():

    root_1 = TreeNode( 2 )
    root_1.left = TreeNode( 1 )
    root_1.right = TreeNode( 3 )

    root_2 = TreeNode( 5 )
    root_2.left = TreeNode( 4 )
    root_2.right = TreeNode( 6 )

    root_of_new_tree = Solution().mergeTrees( root_1, root_2 )

    traverse( root_of_new_tree )

    return 



if __name__ == '__main__':

    test_bench()