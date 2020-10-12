'''

Description:

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]



Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        
        # record of preorder traversal path
        path_of_preorder = []
        
        # Generate pre-order traversal path of binary search tree
        def helper( node ):
            
            if node:
                path_of_preorder.append( node.val )
                helper( node.left )
                helper( node.right )
        
        # ---------------------------------------------
        helper( root )
        # output as string, each node is separated by '#'
        return '#'.join( map(str, path_of_preorder) )
                
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            # corner case handle for empty tree
            return None
        
        # convert input string into doubly linked list of integer type, each node is separated by '#'
        node_values = deque(  int(value) for value in data.split('#') )
        
        # Reconstruct binary search tree by pre-order traversal
        def helper( lower_bound, upper_bound):
            
            if node_values and lower_bound < node_values[0] < upper_bound:
                
                root_value = node_values.popleft()
                root_node = TreeNode( root_value )
                
                root_node.left = helper( lower_bound, root_value )
                root_node.right = helper( root_value, upper_bound )
                
                return root_node
        
        # ---------------------------------------------
        
        return helper( float('-inf'), float('inf'))    


# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of preorder traversal, which is of O( n )

## Space Compelxity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


def inorder( node, path ):

    if node:

        inorder(node.left, path)
        path.append( node.val )
        inorder(node.right, path)

    

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        root = TreeNode( 2 )
        root.left = TreeNode( 1 )
        root.right = TreeNode( 3 )

        result = Codec().deserialize( Codec().serialize(root) )
        path = []
        inorder(node=result, path=path)

        self.assertEqual(path, [1,2,3] )


    def test_case_2( self ):
        
        root = None

        result = Codec().deserialize( Codec().serialize(root) )
        path = []
        inorder(node=result, path=path)

        self.assertEqual(path, [] )




if __name__ == '__main__':

    unittest.main()