'''

Description:

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]



Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]



Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]



Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.



Hint #1  

Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, make sure you are not making multiple copies of the same node.



Hint #2  

You may want to use extra space to keep old node ---> new node mapping to prevent creating multiples copies of same node.



Hint #3  

We can avoid using extra space for old node ---> new node mapping, by tweaking the original linked list. Simply interweave the nodes of the old and copied list. For e.g.

Old List: A --> B --> C --> D
InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'



   Hide Hint #4  
The interweaving is done using next pointers and we can make use of interweaved structure to get the correct reference nodes for random pointers.

'''




# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        # --------------------------------------------------------
        
        # Create mirror node for each node in linked list
        
        cur = head
        
        while cur:
            
            original_next_hop = cur.next
            
            #mirror_node = Node( x = cur.val, next = original_next_hop, random = None)
            
            cur.next = Node( x = cur.val, next = original_next_hop, random = None)
            
            cur = original_next_hop
        
        
        #self.print_linked_list( head )
        
        # --------------------------------------------------------
        
        # Let mirror node get the random pointer
        
        cur = head
        
        while cur:
            
            if cur.random:
                # assign random pointer to mirror node
                cur.next.random = cur.random.next
                
            try:
                # move to next position
                cur = cur.next.next
            except AttributeError:
                break
                
        #self.print_linked_list( head )
        # --------------------------------------------------------
        
        
        # Separate copy linked list from original linked list
        
        try:
            # locate the head node of copy linked list
            head_of_copy_list = head.next
            cur = head_of_copy_list
            
        except AttributeError:
            # original input is an empty linked list
            return None
        
        while cur:
            
            try:
                # link mirror node to copy linked list
                cur.next = cur.next.next
            except AttributeError:
                break
            
            # move to next position
            cur = cur.next
            
        return head_of_copy_list


    # ----------------------------------------------

    # support function to help trace and debugging

    def print_linked_list( self, node ):
        
        cur = node
        
        while cur:
            print( f' val = {cur.val} ')
            
            if cur.next:
                print( f' next = {cur.next.val} ')
            else:
                print( f' next = None ')
                
            if cur.random:
                print( f' random = {cur.random.val} ')
            else:
                print( f' random = None')
                
            print( '\n => \n' )
            
            cur = cur.next



# n : the length of input linked list.

## Time Complexity: O( n )
#
# The overhead in time is the linear scan of linked list, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for ouput linked list, which is of the same length of input, of O( n ).



def test_bench():


    node_7 = Node(7, None, None)
    node_13 = Node(13, None, None)
    node_11 = Node(11, None, None)
    node_10 = Node(10, None, None)
    node_1 = Node(1, None, None)
    
    node_7.next = node_13
    node_7.random = None

    node_13.next = node_11
    node_13.random = node_7

    node_11.next = node_10
    node_11.random = node_1

    node_10.next = node_1
    node_10.random = node_11

    node_1.next = None
    node_1.random = node_7

    head = node_7

    # expected output:
    '''
    val = 7
    next = 13
    random = None

    =>

    val = 13
    next = 11
    random = 7

    =>

    val = 11
    next = 10
    random = 1

    =>

    val = 10
    next = 1
    random = 11

    =>

    val = 1
    next = None
    random = 7

    =>
    '''


    head_of_copy = Solution().copyRandomList( head )

    Solution().print_linked_list( head_of_copy )



if __name__ == '__main__':

    test_bench()    
            
    