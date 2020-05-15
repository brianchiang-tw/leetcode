'''

Description:

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
 

Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        first_minimum = root.val if (root) else (-1)
        
        upper_bound = 2**31
        second_minimum = upper_bound
        
        def helper( node: TreeNode ):
            
            if node:
                        
                helper( node.left )
                helper( node.right )
                
                nonlocal first_minimum, second_minimum
                if node.val != first_minimum:
                    second_minimum = min( second_minimum, node.val)
        
        # -------------------------------------------------------------
        
        helper( root)
        return  second_minimum if second_minimum != upper_bound else -1



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost DFS traversal, which is of O( n )

## Space Comlexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ) 



def test_bench():

    # Test-case #1
    root_1 = TreeNode( 2 )

    root_1.left = TreeNode( 2 )
    root_1.right = TreeNode( 5 )

    root_1.right.left = TreeNode( 5 )
    root_1.right.right = TreeNode( 7 )

    # expected output:
    '''
    5
    '''

    print( Solution().findSecondMinimumValue( root = root_1 ) )

    # -----------------------------------
    # Test-case #2
    root_2 = TreeNode( 2 )
    
    root_2.left = TreeNode(2)
    root_2.right = TreeNode(2)

    # expected output:
    '''
    -1
    '''

    print( Solution().findSecondMinimumValue( root = root_2 ) )



if __name__ == '__main__':

    test_bench()