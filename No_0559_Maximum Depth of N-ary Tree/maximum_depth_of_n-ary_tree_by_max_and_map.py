'''

Description:

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).


Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].

'''



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        else:
            
            return 1 + max( map( self.maxDepth, root.children or [None] ) )



## Time Complexity: O( n )
#
# The overhead in time is the DFS traversal of a n-ary tree, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is to maintain call stack for DFS recursion, which is of O( n )



