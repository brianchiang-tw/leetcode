from collections import deque

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def helper( nestedList: [NestedInteger] ):
            
            for element in nestedList:
                
                if element.isInteger():
                    self.sequence.append( element.getInteger() )
                else:
                    helper( element.getList() )
                    
        # ---------------------------------------                    
                    
        self.sequence = deque()
        helper( nestedList )
    
    
    
    def next(self) -> int:
        
        return self.sequence.popleft()
            
    
    def hasNext(self) -> bool:
        
        return self.sequence



# n : number of integer in the input NestedInteger object.

## Time Complexity: O( n )
#
# For __init__():
# It takes O( n ) to extract integer and put them in 1D list.
#
# For next() and hasNext():
# It takes O( 1 ) to compute and return.

## Space Complexity: O( n )
#
# For __init__():
# It takes O( n ) space to store those input integers in 1D list.
#
# For next() and hasNext():
# It takes O( 1 ) space to compute and output data.