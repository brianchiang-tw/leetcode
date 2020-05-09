'''

Description:

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        
        def helper( node: TreeNode):
            
            root = node
            
            if not node:
                
                # Quick response for empty tree
                return 0
            
            
            height = 0
            while node:
                node = node.left
                height += 1
            
            
            if height == 1:
                
                # Quick response for tree with one level only
                return 1
            
            
            # boundary of node numbering on last level
            
            left, right = 2 ** (height - 1), (2 ** height - 1)
            
            # For complete binary tree, the leftmost node on last level must exist
            
            last_exist = left
            
            
            # Launch binary search to find the numbering of last non-empty node on last level
            
            while left <= right:
                cur = root
                mid = left + (right-left) // 2
                
                # path finding for node with numbering with mid
                for h in range(height-2, -1, -1):
                    
                    mask =  1 << h
                    
                    if mid & mask :
                        cur = cur.right
                        
                    else:
                        cur = cur.left
                    
                    mask >>= 1
                    
                if cur is not None:
                    # update latest finding on last level
                    last_exist = mid
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return last_exist
        
        # -------------------------------
        
        return helper( root )



# n : the number of nodes in binary tree

## Time Complexity: O( (log n )^2 )
#
# The overhead in time is the cost of height of complete binary tree * cost of binary search on bottom level
# It takes O( h ) * O( log n) = O( log n ) * O( log n ) = O( (log n )^2 ) in total.

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which are of O( 1 )


def test_bench():

    root = TreeNode(1)
    
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)

    # expected output:
    '''
    6
    '''

    print( Solution().countNodes(root = root) )

    return



if __name__ == '__main__':

    test_bench()