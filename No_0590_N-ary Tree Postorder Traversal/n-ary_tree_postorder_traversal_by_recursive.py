'''

Description:

Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]

'''



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            # base case:
            # empty node or empty tree
            return []
        
        else:
            # general case:

            path = []

            # Traverse children with postorder:
            for child in root.children:
                path += self.postorder( child )
            
            # Travese current node with postorder:
            path.append( root.val )
            

            return path



# n : the number of nodes in n-ary tree

## Time Complexity: O( n )
#
# The overhead in time is the DFS traversal of a n-ary tree, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for DFS traversal path, which is of O( n ).