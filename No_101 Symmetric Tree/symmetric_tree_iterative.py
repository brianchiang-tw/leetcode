'''

Description:

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def isSymmetric(self, root):
        
        if not root:
            # empty tree
            return True
        
        # initialization
        cur_level_nodes = [ root ]
        next_level_nodes = []
        
        while cur_level_nodes:
            
            cur_level_value = [ node.val if node else None for node in cur_level_nodes ]
            
            
            
            if cur_level_value != cur_level_value[::-1]:
                # check symmetry on current level
                # symmetric <=> inorder is equal to reverse order
                return False

            next_level_nodes.clear()
            
            for node in cur_level_nodes:
                
                if node:
                    # append children nodes to next_level_nodes
                    next_level_nodes.append( node.left )
                    next_level_nodes.append( node.right )
            

            # update cur_level_nodes as next_level_nodes
            cur_level_nodes = next_level_nodes[:]
            
        return True
            


# N : number of elements in binary tree

## Time Complexity: O( N )
#
# The overhead in time is the recusion to check each level.
# Visit each single node takes O(1).
# There are n nodes in total, thus take O(N) for whole tree.

## Space Complexity: O(  N )
#
# The overhead is space is to maintain cur_level_nodes and next_level_nodes.
# There are n nodes in total, thus take O(N) for whole tree.
        
def test_bench():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    is_symmetric = Solution().isSymmetric( root )
    
    # expected output:
    '''
    True
    '''
    print( is_symmetric )

    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)

    is_symmetric = Solution().isSymmetric( root )

    # expected output:
    '''
    False
    '''
    print( is_symmetric )

    return



if __name__ == '__main__':

    test_bench()