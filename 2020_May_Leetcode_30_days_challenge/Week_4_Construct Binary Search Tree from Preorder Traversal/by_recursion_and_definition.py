'''

Description:

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        root_index = 0
        
        def helper( preorder, upperbound):
            
            nonlocal root_index
            
            if root_index == len(preorder) or preorder[root_index] > upperbound:
                return None
            
            root = TreeNode( preorder[root_index] )
            
            # update root index by adding one
            root_index += 1
            
            root.left = helper( preorder, root.val )
            root.right = helper( preorder, upperbound )

            return root
                
        return helper( preorder, float('inf') )



# n : number of nodes in binary tree

## Time complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'pre_order_path')


def print_level_order( node:TreeNode ):

    traversal_queue = [ node ] if node else []

    while traversal_queue:

        next_level_queue = []

        for cur_node in traversal_queue:

            if cur_node:
                print(f'{cur_node.val}', end = ' ')

                if cur_node.left or cur_node.right:
                    next_level_queue.append( cur_node.left )
                    next_level_queue.append( cur_node.right )

            else:
                print(f'None', end = ' ')
            


        traversal_queue = next_level_queue

    return



def test_bench():

    result = Solution().bstFromPreorder( [8,5,1,7,10,12] )

    # expected output:
    '''
    8 5 10 1 7 None 12
    '''

    print_level_order( result )



if __name__ == '__main__':

    test_bench()