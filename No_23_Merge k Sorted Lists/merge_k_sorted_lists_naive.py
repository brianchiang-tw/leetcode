# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        
        # linked list for solution storage
        # head_of_solution = ListNode( None )
        head_of_solution = None
        
        # a support list to keep sorted value in order
        solution = list()
        
        while( True ):
            
            # generate valid list, excluding empty linked list
            #valid_list = [ node for node in lists if node is not None]
            
            lists = [ node for node in lists if node is not None]
            
            #if len( valid_list) == 0:
            if len( lists ) == 0:
                # all element has been sorted
                break
            
            
            # get the list of min value
            #list_of_min = min( valid_list, key = lambda node: node.val)
            list_of_min = min( lists, key = lambda node: node.val)
            
            # get min value
            min_value_across_list = list_of_min.val

            # add min value into solution
            solution.append( min_value_across_list )
            
            # get index
            index_of_list_of_min = lists.index( list_of_min )


            # pop min value from input
            # update head as head's next
            lists[ index_of_list_of_min ] = lists[ index_of_list_of_min ].next
            
        
        # message for tracing and debugging
        #for x in solution:
        #    print( x )
        
        # generate linklist of solution by reverse order ( by creating solution linked list from max value to min value )   
        for i in range( len(solution)-1, -1, -1):
            
            head_of_solution = self.insert_min( head_of_solution, solution[i] )
            
    
        return head_of_solution
    
    
    
    def insert_min( self, head_node, value ):
        
        #if head_node.val is None:
        if head_node is None:
            # if linklist is empty
            # insert at head node directly
            head_node = ListNode( value)
            # head_node.val = value 
            
            return head_node
            
        else:
            # if linklistis non-empty
            # insert new node beforehand
            new_node = ListNode( value )
            
            # update new_node's next as head_node
            new_node.next = head_node
            
            return new_node
            
        