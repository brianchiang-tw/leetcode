'''

Description:

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

'''



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        path_of_preorder = []
        
        def encoder( node: TreeNode):
            
            if node:
                
                path_of_preorder.append( node.val )
                
                encoder( node.left )
                encoder( node.right )

            else:
                
                path_of_preorder.append( '3.14' )
        
        # ------------------------------------------------
        encoder( root )
        
        codec = '#'.join( map( str, path_of_preorder ) )
        
        return codec
        

        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        path_of_preorder = deque( float(value) for value in data.split('#') )
        
        def decoder():
            
            if path_of_preorder:
                
                value = path_of_preorder.popleft()
                
                if value != 3.14:
                
                    cur_node = TreeNode( int(value) )

                    cur_node.left = decoder()
                    cur_node.right = decoder()
                    
                    return cur_node
                
                else:
                    
                    return None
        # -----------------------------------
        return decoder()



# n : the number of node in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of preorder traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the cost of recursion call stack, which is of O( n ).


def in_order( node ):

    if node:

        in_order( node.left )
        print( node.val, end = ' ')
        in_order( node.right )


def test_bench():

    root_1 = TreeNode( 1 )
    
    root_1.left = TreeNode( 2 )
    root_1.right = TreeNode( 3 )

    root_1.right.left = TreeNode( 4 )
    root_1.right.right = TreeNode( 5 )


    # expected output:
    '''
     before :
    2 1 4 3 5
     after :
    2 1 4 3 5
    '''

    # Before serialization and deserialization:
    print(" before : ")
    in_order( root_1 )
    
    serialization =  Codec().serialize( root_1 ) 
    root_of_tree = Codec().deserialize( serialization )
    print("\n after : ")
    # After serialization and deserialization:
    in_order( root_of_tree )

    return



if __name__ == '__main__':

    test_bench()