# Note:
# Taking time and space complexity into consideration, 
# this implementation is not good enough.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def helper( node: TreeNode, target:int) -> bool:
            
            left_removal = False
            right_removal = False
            
            if node:
                # current node exists
                
                if not node.left and not node.right:
                    # current node is leaf
                    
                    if node.val == target:
                        # current node is leaf with target
                        node = None
                        return (True, None)
                    else:
                        # current node is leaf but without target value
                        return (False, node)
                
                else:
                    # current node is non-leaf
                    
                    if node.left:
                        # check left child
                        
                        if not node.left.left and not node.left.right:
                            
                            if node.left.val == target:
                                node.left = None
                                left_removal = True
                            
                        else:
                            left_removal, _ = helper(node.left, target)
                            
                            
                    if node.right:
                        # check right child
                        
                        if not node.right.left and not node.right.right:
                            
                            if node.right.val == target:
                                node.right = None
                                right_removal = True
                            
                        else:
                            
                            right_removal, _ = helper(node.right, target)
                        
                    return ((left_removal or right_removal), node)
            else:
                # current node is None
                return (False, node)
        
        
        cur_root = root
        while True:
            has_removal, cur_root = helper(cur_root, target)
            
            if not has_removal:
                break
                
        return cur_root