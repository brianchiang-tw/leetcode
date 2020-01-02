'''

Description:

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.


        7
      /   \
     3     15
          /  \
         9    20 



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.


'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class BSTIterator:

    def __init__(self, root: TreeNode):

        self.root = root
        self.elements = deque()
        self.inorder( root )
        
    
    def inorder(self, node: TreeNode):
        
        if node:
            
            self.inorder( node.left )
            self.elements += [ node.val ]
            self.inorder( node.right )
            
            

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.elements.popleft()
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.elements) != 0



# N : number of elements in binary tree

## Time Complexity: O( 1 )
#
# The overhead on time is to traverse all node with inorder of O( N ) on constructor __init__
# But the amortized for n next() call is O(1) actually.

## Space Complexity: O( N )
#
# THe overhead in space is to maintain a list to store all the elements with inorder on ( N )



def test_bench():

    '''
              7
            /   \
           3     15
                /  \
               9    20 
    '''

    root = TreeNode( 7 )

    root.left = TreeNode( 3 )
    root.right = TreeNode( 15 )

    root.right.left = TreeNode( 9 )
    root.right.right = TreeNode( 20 )


    iterator = BSTIterator(root)


    # expected output:
    '''
    3
    7
    True
    9
    True
    15
    True
    20
    False
    '''


    test_operation = [
                    "iterator.next()",
                    "iterator.next()",
                    "iterator.hasNext()",
                    "iterator.next()",
                    "iterator.hasNext()",                    
                    "iterator.next()",
                    "iterator.hasNext()",
                    "iterator.next()",
                    "iterator.hasNext()",

                ]

    for operation in test_operation:

        print( eval(operation) )

    return



if __name__ == '__main__':

    test_bench()