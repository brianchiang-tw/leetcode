'''

Description:

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.

 

Example 1:

Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.



Example 2:

Input: tree = [7], target =  7
Output: 7



Example 3:

Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4



Example 4:

Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
Output: 5



Example 5:

Input: tree = [1,2,null,3], target = 2
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.


'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def helper( node: TreeNode, cloned: TreeNode):
            
            if node is target:
                yield cloned
            
            if node.left:
                yield from helper( node.left, cloned.left )
            
            if node.right:
                yield from helper( node.right, cloned.right )
                
        # -------------------------------------------------------------------
        return next( helper(original, cloned) )



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of pre-order DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).



def clone_tree( node: TreeNode ):

        if node is not None:
            cur = TreeNode( node.val )
            cur.left = clone_tree( node.left )
            cur.right = clone_tree( node.right )

            return cur
        else:
            return None



def test_bench():

    root_1 = TreeNode( 7 )
    root_1.left = TreeNode( 4 )
    root_1.right = TreeNode( 3 )
    root_1.right.left = TreeNode( 6 )
    root_1.right.right = TreeNode( 19 )

    root_1_clone = clone_tree( root_1 )
    target = root_1.right

    
    # expected output:
    '''
    3
    '''
    target_clone =  Solution().getTargetCopy( root_1, root_1_clone, target )
    print( target_clone.val )



if __name__ == '__main__':

    test_bench()