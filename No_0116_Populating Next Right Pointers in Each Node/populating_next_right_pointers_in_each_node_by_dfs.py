'''

Description:

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [1,#,2,3,#,4,5,6,7,#]

Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def helper( node: 'Node'):
            
            if node and node.left and node.right:
                
                # update next of left child        
                node.left.next = node.right
                
                # update next of right child
                if node.next:
                    node.right.next = node.next.left
            
                helper( node.left )
                helper( node.right )
            
            return node
        # ----------------------------
        
        return helper( root )



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n )

## Space Complexity: O( n ) in total, O( 1 ) in aux space
#
# The overhead in space is the storage for call stack.
# The aux space is temporary node, which is of O( 1 ).


from collections import deque
def print_level_order_traversal( node ):

    traversal_queue = deque([node])

    while traversal_queue:

        leftmost = traversal_queue.popleft()
        cur_node = leftmost

        while cur_node:
            print(f'{cur_node.val} ', end = '')
            cur_node = cur_node.next
        
        print('# ', end = '')

        if leftmost.left:
            traversal_queue.append( leftmost.left )


def test_bench():

    # Test Case_#1
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)

    root_1 = node_1
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    root_1 = Solution().connect(root_1)

    # expected output:
    '''
    1 # 2 3 # 4 5 6 7 # 
    '''

    print_level_order_traversal( root_1 )


    return



if __name__ == '__main__':

    test_bench()