# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from collections import deque

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
    
        def helper( nestedList: [NestedInteger] ):
            
            for element in nestedList:
                
                if element.isInteger():
                    yield element.getInteger()
                else:
                    yield from helper( element.getList() )

            
        
        
        #self.list_iterator = 
        self.sequence = deque( helper( nestedList ) )
        
    
    
    def next(self) -> int:
        
        return self.sequence.popleft()
            
    
    def hasNext(self) -> bool:
        
        return self.sequence
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())



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