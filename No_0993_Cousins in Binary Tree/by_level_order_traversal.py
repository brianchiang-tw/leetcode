'''

Description:

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false



Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true



Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import namedtuple

# first parameter is parnet node
# second parameter is the level of current node

Entry = namedtuple( 'Entry', 'parent level')

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        # Let general case handle root node
        dummy_head = TreeNode(-1)
        dummy_head.left = root
        
        traversal_queue = [ (dummy_head, 0) ]
        x_info, y_info = None, None
        
        while traversal_queue:
            
            next_level_queue = []
            
            for cur_node, cur_level in traversal_queue:
                
                for child in ( cur_node.left, cur_node.right):
                    
                    if child:
                        
                        # update information of parent and level for x and y
                        if child.val == x:
                            x_info = Entry( parent = cur_node, level = cur_level+1 )
                            
                        elif child.val == y:
                            y_info = Entry( parent = cur_node, level = cur_level+1 )
                        
                        # update next level traversal queue
                        next_level_queue.append( (child, cur_level+1) )
                               
            
            traversal_queue = next_level_queue
            

        return (x_info.parent is not y_info.parent) and (x_info.level == y_info.level)



# n : the nubmer of node in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of level-order traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal queue, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'root x y')

def test_bench():

    root_1 = TreeNode( 1 )

    root_1.left = TreeNode( 2 )
    root_1.right = TreeNode( 3 )

    root_1.left.left = TreeNode( 4 )

    x_1, y_1 = 4, 3
    # --------------------------------

    root_2 = TreeNode( 1 )

    root_2.left = TreeNode( 2 )
    root_2.right = TreeNode( 3 )

    root_2.left.right = TreeNode( 4 )
    root_2.right.right = TreeNode( 5 )

    x_2, y_2 = 5, 4
    # --------------------------------

    root_3 = TreeNode( 1 )

    root_3.left = TreeNode( 2 )
    root_3.right = TreeNode( 3 )

    root_3.left.right = TreeNode( 4 )

    x_3, y_3 = 2, 3

    # --------------------------------

    test_data = [ 
                    TestEntry( root = root_1, x = x_1, y = y_1 ),
                    TestEntry( root = root_2, x = x_2, y = y_2 ),
                    TestEntry( root = root_3, x = x_3, y = y_3 ),
                ]

    # expected output:
    '''
    False
    True
    False
    '''

    for t in test_data:

        print( Solution().isCousins( *t ) )

    return



if __name__ == '__main__':

    test_bench()