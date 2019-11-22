# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
            
            

    
import heapq

class Solution:
    def mergeKLists(self, lists ):

        
        # dummy head node
        head_node = ListNode(0)
        insert_position = head_node
    
        min_heap = list()
    
    
        for node in lists:
            
            if node is not None:
                
                # push each valid node into min heap with
                # 1. node value
                # 2. id(node), as a tie-breaker when any two nodes' value is the same
                # 3. node
                heapq.heappush( min_heap, (node.val, id(node), node) )
                
        
        
        while len(min_heap) != 0:
            
            # get minimal value and node of min value from min heap
            min_value, node_id, min_node = heapq.heappop( min_heap )
            
            # make new node append to insert position's next
            insert_position.next = ListNode( min_value )
            
            # update insert position
            insert_position = insert_position.next
            
            # update the first node of linked list with min_value as the next one
            min_node = min_node.next
            
            
            # if min_node is within a valid linked list, then put it back to min heap
            if min_node is not None:
                
                heapq.heappush( min_heap, (min_node.val, id(min_node), min_node) )
               
        
        head_node_of_solution = head_node.next
        
        return head_node_of_solution
            
            
                
def test_bench():

    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    list3 = ListNode(2)
    list3.next = ListNode(6)
        
    head_of_solution = Solution().mergeKLists( [list1, list2, list3] )

    # print out solution
    current = head_of_solution
    while current is not None:

        print( current.val )

        # update current
        current = current.next


    return 
    
if __name__ == "__main__":

    test_bench()