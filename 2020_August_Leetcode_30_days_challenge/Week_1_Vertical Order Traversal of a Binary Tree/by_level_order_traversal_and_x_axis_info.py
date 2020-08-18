'''

Description:

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).



Example 2:

Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List
from collections import defaultdict
from bisect import insort

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        traversal_queue = [(root, 0)] if root else []
        
        result = []
        
        ## global dictionary to record x-axis value and corresponding node value
        # key: x-axis value
        # value: a list of node value with specified x-axis value
        x_nodeval_dict = defaultdict(list)
        
        # launch level-order traversal
        while traversal_queue:
            
            next_level_queue = []
            
            # local dictionary for current level
            cur_level_dict = defaultdict(list)
            
            for node, x_axis_val in traversal_queue:
            
                # put node value to local dictionary in ascending order
                insort( cur_level_dict[x_axis_val], node.val )
                
                if node.left:
                    next_level_queue.append( (node.left, x_axis_val - 1) )
                
                if node.right:
                    next_level_queue.append( (node.right, x_axis_val + 1) )

            
            # update global dictionary with local dictionary
            for x_axis_value in cur_level_dict:
                x_nodeval_dict[x_axis_value].extend( cur_level_dict[x_axis_value] )

            # update traversal queue for next level            
            traversal_queue = next_level_queue
            

        # output key-value pair based on x-axis value in ascending order
        for x_axis_value in sorted( x_nodeval_dict.keys() ):
            result.append( x_nodeval_dict[x_axis_value] )
        
        
        return result


# n : the number of nodes in binary tree

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of BFS with bisection, which is of O( n log n)

## Space Complexity: O( n )
#
# The overhead in space is the storage for result output, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        root = TreeNode(1)

        root.left = TreeNode(2)
        root.right = TreeNode(3)

        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        result = Solution().verticalTraversal( root=root )
        self.assertEqual(result, [[4],[2],[1,5,6],[3],[7]])



if __name__ == '__main__':

    unittest.main()
