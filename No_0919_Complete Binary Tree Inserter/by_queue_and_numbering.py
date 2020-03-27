'''

Description:

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
 

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]
 

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class CBTInserter:

    
    def __init__(self, root: TreeNode):
        
        self.root = root
        
        self.parent_keeper = deque([root])

        while True:
            
            cur = self.parent_keeper[0]
            
            if cur:
                
                if cur.left:
                    
                    self.parent_keeper.append( cur.left )
                    
                    if cur.right:
                        
                        self.parent_keeper.append( cur.right )
                        
                        # cur is completed with two child, pop out
                        self.parent_keeper.popleft()
                    
                    else:
                        # parent of next insertion is found, stop
                        break
                
                else:
                    # parent of next insertion is found, stop
                    break
        
        

    def insert(self, v: int) -> int:
        
        # Get parent for insertion
        parent = self.parent_keeper[0]
        
        if not parent.left:
            parent.left = TreeNode( v )
            self.parent_keeper.append( parent.left )
        else:
            parent.right = TreeNode( v )
            self.parent_keeper.append( parent.right )
            
            # current parent is completed with two child now, pop parent from parent keeper on the head
            self.parent_keeper.popleft()
            
        return parent.val
        

    def get_root(self) -> TreeNode:
        
        return self.root



# n : the number of nodes in complete binary tree

## Time Complexity:
#
# O( n ) for __init()__
# O( 1 ) for insert()
# O( 1 ) for get_root()

## Space Complexity:
#
# O( n ) for __init()__
# O( 1 ) for insert()
# O( 1 ) for get_root()


