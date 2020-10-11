'''

Description:

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:



Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]



Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.

'''




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root:
            # stop condition:
            # empty tree
            root = TreeNode(val)
            
        
        else:
            # Insert with BST ordering property
            
            if val > root.val:
                
                if root.right:
                    # general case:
                    self.insertIntoBST(root.right, val)
                    
                else:
                    # stop condition:
                    root.right = TreeNode(val)
                    
            else:
                if root.left:
                    # general case:
                    self.insertIntoBST(root.left, val)
                    
                else:
                    # stop condition:
                    root.left = TreeNode(val)
            
            
        return root



# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of insertion, which is of O( n )

## Space Comeplxity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


