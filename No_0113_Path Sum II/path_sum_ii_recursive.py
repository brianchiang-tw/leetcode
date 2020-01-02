# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check_path_sum( self, node: TreeNode, sum, path: List[int], solution):
        
        if node is None:
            # empty tree
            return

        if node.val == sum and node.left is None and node.right is None:
            
            # get one solution meets summation requirement
            # add current node to path
            path += [ node.val ]
            
            # add current path to solution
            solution += [ path[:] ]
            
            return
        
        else:
            
            # update sum for next level
            sum -= node.val
            
            # add current node to path
            path += [ node.val ]
            
            # dfs with left child
            self.check_path_sum( node.left, sum, path[:], solution)
            
            # dfs with right child
            self.check_path_sum( node.right, sum, path[:], solution)
        
            return
        
        
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        solution = [] 
        
        self.check_path_sum( root, sum, [], solution )
        
        return solution
        
        