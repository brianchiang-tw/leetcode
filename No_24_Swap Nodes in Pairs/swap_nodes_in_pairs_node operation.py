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
        
        # corner case handling:
        # Empty list or list with one node just return itself
        if head is None or head.next is None:
            return head
        
        
        # general case:
        dummy_head = ListNode(0)
        previous = dummy_head
        
        
        # check linked list still has more than two nodes
        while head and head.next:
            
            # original_first is head
            
            # get original second
            original_second = head.next
            
            # major operation_#1
            # makes original first's next point to original_second'next
            head.next = original_second.next
            
            # major operation_#2
            # makes original_seconds's next point to original first
            original_second.next = head
            
            # major operation_#3
            # update previous' next as original second
            previous.next = original_second
            
            # update previous position
            previous = head
            
            # update head position
            head = head.next
        
        return dummy_head.next



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