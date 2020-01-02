from collections import deque

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        numbers = deque( list( range( len(S)+1 ) ) )
        
        output = []
        
        for ch in S:
            
            if ch == 'I':
                # Increaing, select min, and push it into output
                output.append( numbers.popleft() )
                
            else:
                # Decreasing, select Max, and push it into output
                output.append( numbers.pop() )
                
    
        # last element
        output.append( numbers.pop() )
        
        return output