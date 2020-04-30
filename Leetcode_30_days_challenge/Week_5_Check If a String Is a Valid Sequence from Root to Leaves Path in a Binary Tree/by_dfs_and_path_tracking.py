'''

Description:

Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

 

Example 1:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation: 
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
Other valid sequences are: 
0 -> 1 -> 1 -> 0 
0 -> 0 -> 0
Example 2:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false 
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
Example 3:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
 

Constraints:

1 <= arr.length <= 5000
0 <= arr[i] <= 9
Each node's value is between [0 - 9].
   Hide Hint #1  
Depth-first search (DFS) with the parameters: current node in the binary tree and current position in the array of integers.
   Hide Hint #2  
When reaching at final position check if it is a leaf node.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        
        def helper( node: TreeNode, path: List[int] ):
            '''
            Input:
            node, (TreeNode)    : current traversal node
            path, (List[int])   : a list to record the root-to-node path
            
            Output:
            True if arr is a valid root-to-leaf path
            False, otherwise
            '''
            
            
            if node:

                left, right = False, False
                
                if (not node.left) and (not node.right):
                    
                    # Base case:
                    # Now it is leaf node, judge whether arr is a valid root-to-leaf path
                    
                    return ( arr == ( path + [node.val] ) )
                           
                elif not node.left and node.right:
                    right = helper( node.right, path + [ node.val ] )    
                    
                elif not node.right and node.left:
                    left = helper( node.left, path + [ node.val] )
                    
                else:
                    left = helper( node.left, path + [ node.val ] )    
                    right = helper( node.right, path + [ node.val ] )    
                    
                return left or right
  
        # --------------------------------------------------

        return helper( root, [] )



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )
