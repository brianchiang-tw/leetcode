'''

Description:

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.



Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 


Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

'''




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        if not root:
            # Quick response for empty tree
            return False
        
        num_set = set()
        
        traversal_stack = [ (root, 'init') ]
        
        has_solution = False
        while traversal_stack:
            
            node, label = traversal_stack.pop()
            
            if label != 'c':
                
                if node.right:
                    traversal_stack.append( (node.right, 'r') )
                    
                traversal_stack.append( (node, 'c') )
                
                if node.left:
                    traversal_stack.append( (node.left, 'l') )
            
            else:
                
                if node.val in num_set:
                    
                    has_solution = True    
                    break
                
                num_set.add( k-node.val )
        
        return has_solution
                    


# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for set, num_set, which is of O( n )



def test_bench():

    ## Test_case_#1
    root_1 = TreeNode(5)

    root_1.left = TreeNode(3)
    root_1.right = TreeNode(6)

    root_1.left.left = TreeNode(2)
    root_1.left.right = TreeNode(4)
    root_1.right.right = TreeNode(7)
    # expected output:
    '''
    True
    '''
    print( Solution().findTarget(root = root_1, k = 9) )



    ## Test_case_#2
    root_1 = TreeNode(5)

    root_1.left = TreeNode(3)
    root_1.right = TreeNode(6)

    root_1.left.left = TreeNode(2)
    root_1.left.right = TreeNode(4)
    root_1.right.right = TreeNode(7)
    # expected output:
    '''
    False
    '''
    print( Solution().findTarget(root = root_1, k = 28) )


if __name__ == '__main__':

    test_bench()

