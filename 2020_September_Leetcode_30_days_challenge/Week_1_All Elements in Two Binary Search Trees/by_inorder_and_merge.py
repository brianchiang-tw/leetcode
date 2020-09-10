# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from collections import deque

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        # -------------------------------------
        
        def dfs(node):
            
            if node:
                
                yield from dfs(node.left)
                yield node.val
                yield from dfs(node.right)
                
        # -------------------------------------
        
        l1 = deque( [*dfs(root1)] )
        l2 = deque( [*dfs(root2)] )
        
        result = []
        
        while l1 and l2:
            
            if l1[0] < l2[0]:
                
                result.append( l1.popleft() )
                
            else:
                
                result.append( l2.popleft() )
        
        while l1:
            result.append( l1.popleft() )
            
        while l2:
            result.append( l2.popleft() )
        
        return result



# m : the number of nodes in the first binary search tree
# n : the number of nodes in the second binary search tree 

## Time Comeplexity: O( m + n )
#
# The overhead in time is the cost of DFS and merging process, which is of O( m + n )

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for result output, which is of O( m + n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        root1 = TreeNode( 2 )
        root1.left = TreeNode( 1 )
        root1.right = TreeNode( 4 )

        root2 = TreeNode( 1 )
        root2.left = TreeNode( 0 )
        root2.right = TreeNode( 3 )

        result = Solution().getAllElements(root1=root1, root2=root2)
        self.assertEqual(result, [0, 1, 1, 2, 3, 4])



    def test_case_2( self ):

        root1 = TreeNode( 0 )
        root1.left = TreeNode( -10 )
        root1.right = TreeNode( 10 )

        root2 = TreeNode( 5 )
        root2.left = TreeNode( 1 )
        root2.right = TreeNode( 7 )
        root2.left.left = TreeNode( 0 )
        root2.left.right = TreeNode( 2 )

        result = Solution().getAllElements(root1=root1, root2=root2)
        self.assertEqual(result, [-10,0,0,1,2,5,7,10])


    def test_case_3( self ):

        root1 = None

        root2 = TreeNode( 5 )
        root2.left = TreeNode( 1 )
        root2.right = TreeNode( 7 )
        root2.left.left = TreeNode( 0 )
        root2.left.right = TreeNode( 2 )

        result = Solution().getAllElements(root1=root1, root2=root2)
        self.assertEqual(result, [0,1,2,5,7])


    def test_case_4( self ):

        root1 = TreeNode( 0 )
        root1.left = TreeNode( -10 )
        root1.right = TreeNode( 10 )

        root2 = None

        result = Solution().getAllElements(root1=root1, root2=root2)
        self.assertEqual(result, [-10,0,10])


if __name__ == '__main__':

    unittest.main()        