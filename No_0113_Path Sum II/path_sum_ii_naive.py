'''

Description:

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def check_path_sum( self, node: TreeNode, sum, path: List[int]):
        
        
        
        if node:
            
            if node.val == sum and node.left is None and node.right is None:
                
                cur_path = path + [ node.val ]
                
                #print("{} is meet, return {}". format( node.val, str([cur_path]) ) )
                return True, [cur_path]
            

            else:
                
                next_path = path + [ node.val ]
                
                left_flag, left_sol = self.check_path_sum( node.left, sum-node.val, next_path)
                right_flag, right_sol = self.check_path_sum( node.right, sum-node.val, next_path)
                    
                path_container = [ ]
                
                #print("\n\n current node value: {}".format(node.val))
                #print("left flag = {}, left sol={}".format( left_flag, left_sol) )
                #print("right flag = {}, right sol={}".format( right_flag, right_sol) )
            
                if left_flag is True and right_flag is True:
                    
                    path_container += [  p for p in left_sol ]
                    path_container += [  p for p in right_sol ]
                    
                    #print("return path container: {}".format( path_container) )
                    return True, path_container[:]
                    
                elif left_flag is True:
                    
                    sol_and_cur = [  p for p in left_sol ]
                    #print("sol and cur: {}".format( sol_and_cur ) )
                    
                    path_container += sol_and_cur
                    
                    #print("return path container: {}".format( path_container) )
                    return True, path_container[:]
                
                elif right_flag is True:
                    
                    sol_and_cur = [  p for p in right_sol ]
                    #print("sol and cur: {}".format( sol_and_cur ) )
                          
                    path_container += sol_and_cur
                          
                    #print("return path container: {}".format( path_container) )
                    return True, path_container[:]
                else:
                    return False, []
                
        else:
            # empty node or empty tree
            return False, []
    
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        flag, solution = self.check_path_sum( root, sum, [] )
        
        if flag:
            return solution
        else:
            return []
        