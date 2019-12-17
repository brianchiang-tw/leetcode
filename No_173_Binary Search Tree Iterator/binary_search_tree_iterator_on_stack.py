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


class BSTIterator:

    def __init__(self, root: TreeNode):

        self.root = root
        self._stack_inorder = []

        self.push_left_children( root )
        
    
    def push_left_children(self, node: TreeNode):
        
        while node:
            # push left child into stack
            self._stack_inorder.append( node )

            # update node as left child
            node = node.left

            
            

    def next(self) -> int:
        """
        @return the next smallest number
        """

        # pop next element with inorder
        node =  self._stack_inorder.pop()

        # keep inorder collection on right subtree of node
        self.push_left_children( node.right )

        return node.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self._stack_inorder) != 0



# N : number of elements in binary tree
# h : hight of the binary tree

## Time Complexity: O( 1 )
#
# The overhead on time is to push_left_children during each next()
# Indeed, push_left_children takes O( N ) when worst case of skew tree at one node.
# However, push_left_children worst case won't happen at every node, after amortized for n next() calling, it is O( 1 )

## Space Complexity: O( h )
#
# THe overhead in space is to maintain a stack to store all the left childrean with inorder on ( h )



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