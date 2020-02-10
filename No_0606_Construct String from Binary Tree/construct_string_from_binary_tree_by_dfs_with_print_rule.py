'''

Description:

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    
    # update DFS pre-oreder traversal path with print rule
    def helper( self, node, path):
            
        if node:
            # left coat brace of current node
            path.append('(')

            # value of current node
            path.append( str( node.val ) )

            if node.left or (not node.left and node.right):
                # left sub-tree cannot be skipped if right sub-tree exists
                self.helper( node.left, path )

            if node.right:
                # print right sub-tree only when it is non-empty node
                self.helper( node.right, path )

            # right coat brace of current node
            path.append(')')

        else:
            # empty node or empty tree
            path.append('(')
            path.append(')')
            return
    
    
    
    def tree2str(self, t: TreeNode) -> str:            

        # record of DFS pre-oreder traversal    
        path = []

        # DFS pre-oreder traversal 
        self.helper( t, path )
        
        # [1:-1] slicing is to remove the outer-most braces of root node
        return ''.join(path[1:-1])



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of variant pre-order DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the recusrion call stack, and the output string, which are of O( n ).



def test_bench():

    root = TreeNode(4)

    root.left = TreeNode(2)
    root.right = TreeNode(6)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right.right = TreeNode(7)

    # expected output:
    '''
    4(2(1)(3))(6()(7))
    '''
    print( Solution().tree2str(root) )

    return 
    


if __name__ == '__main__':

    test_bench()    