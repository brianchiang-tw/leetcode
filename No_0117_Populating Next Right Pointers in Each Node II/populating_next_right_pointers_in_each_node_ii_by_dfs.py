'''

Description:

Given a binary tree

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



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100

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
                
            scanner = node.next

            # Scanner finds left-most neighbor, on same level, in right hand side
            while scanner:

                if scanner.left:
                    scanner = scanner.left
                    break

                if scanner.right:
                    scanner = scanner.right
                    break

                scanner = scanner.next


            # connect right child if right child exists
            if node.right:
                node.right.next = scanner 

            # connect left child if left child exists
            if node.left:
                node.left.next = node.right if node.right else scanner


            # DFS down to next level
            if node.right:
                helper( node.right )

            if node.left:
                helper( node.left )
                
            return node
        # -------------------------------
        
        if not root:
            return None
        
        else:
            return helper( root ) 



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n )

## Space Complexity: O( n ) in total, O( 1 ) in aux space
#
# The overhead in space is the storage for call stack, which is of O( n ).
# The aux space is temporary node, which is of O( 1 ).

from collections import deque
def print_level_order_traversal( node: 'Node' ):

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

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_7 = Node(7)

    root_1 = node_1

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.right = node_7

    root_1 = Solution().connect( root_1 )

    print_level_order_traversal( root_1 )

    # expected output:
    '''
    1 # 2 3 # 4 5 7 #
    '''

    return



if __name__ == '__main__':

    test_bench()
