'''

Description:

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint #1  
Try to utilize the property of a BST.



Hint #2  
Try in-order traversal. (Credits to @chan13)



Hint #3  
What if you could modify the BST node's structure?



Hint #4  
The optimal runtime complexity is O(height of BST).

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        traversal_timestamp = 0
        traversal_stack = [ (root, 'init')]
        kth_element = None
        
		# in-order traversal
        while traversal_stack:
            
            node, label = traversal_stack.pop()
            
            if node:
                
                if label is not 'c':
                
                    if node.right:
                        traversal_stack.append( (node.right, 'r') )
                    
                    traversal_stack.append( (node, 'c') )
                    
                    if node.left:
                        traversal_stack.append( (node.left, 'l') )
                
                else:
                    
                    traversal_timestamp += 1
                    
                    if traversal_timestamp == k:
                        # Catch the kth smallest element
                        kth_element = node.val
                        break
        
        return kth_element



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of in-order traversal, which is of O( n ) at most

## Space Complexity: O( n )
# 
# The overhead in space is the storage for traversal queue, which is of O( n ) 

from collections import namedtuple
TestEntry = namedtuple('TestEntr', 'root k')
def test_bench():

    ## Test_case_#1

    root_1 = TreeNode(3)
    root_1.left = TreeNode(1)
    root_1.right = TreeNode(4)
    root_1.left.right = TreeNode(2)

    t = TestEntry( root = root_1, k=1 )
    # expected output:
    '''
    1
    '''
    print( Solution().kthSmallest( root = t.root, k = t.k ) )

    ## Test_case_#2

    root_2 = TreeNode(5)

    root_2.left = TreeNode(3)
    root_2.right = TreeNode(6)

    root_2.left.left = TreeNode(2)
    root_2.left.right = TreeNode(4)

    root_2.left.left.left = TreeNode(1)

    t = TestEntry( root = root_2, k = 3 )

    # expected output:
    '''
    3
    '''
    print( Solution().kthSmallest( root = t.root, k = t.k) )




    return



if __name__ == '__main__':

    test_bench()    