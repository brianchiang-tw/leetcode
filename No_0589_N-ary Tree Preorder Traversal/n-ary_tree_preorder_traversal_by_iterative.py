class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        # base_case:
        traverse_stack = [root]
        path = []
        
        # general case:
        while traverse_stack:
            
            current = traverse_stack.pop()
            
            if current:
                
                # Travese current node with preorder:
                path.append( current.val )
                

                if not current.children:
                    continue
                
                
                # Traverse children with preorder:
                # Left part if of higher priority than right part.
                # Thus, push right part before left part.
                for i in range( len(current.children)-1, -1, -1 ):
                    traverse_stack.append( current.children[i] )
                
        return path



# n : the number of nodes in n-ary tree

## Time Complexity: O( n )
#
# The overhead in time is the DFS traversal of a n-ary tree, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for DFS traversal path, which is of O( n ).