'''
Description:

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        cur = head
               
        try:
            
            # locate head of next pair
            next_pair = cur.next.next
            
            # reverse next pair
            junction = self.swapPairs( next_pair )
            
            # reverse current pair
            original_next = cur.next
            
            original_next.next = cur
            
            # build new linkage from current pair to next pair
            cur.next = junction
            
            return original_next
            
        except:
            
            # Base case:
            # Either one node or None remaining
            return cur



# N : total number of element in all lists

 # Time complexity
 # O( N )       
 # Each node pair swap take O(1) constant node operation
 # For N nodes, there are O(N//2) node pairs

 # To sum up, overall time complexity is O (N)


 # Space complexity
 # O( N ) for saving all elements in the form of linked list


        
    
def test_bench():

    head = ListNode(1)

    head.next = ListNode(2)

    head.next.next = ListNode(3)

    head.next.next.next = ListNode(4)

    head_of_solution = Solution().swapPairs( head )

    # print out solution
    current = head_of_solution
    while current is not None:

        print( current.val )

        current = current.next

    # expected output
    '''
    2
    1
    4
    3
    '''




if __name__ == "__main__":

    test_bench()