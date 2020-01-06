class Solution:
    
    def helper(self, s, k):
        
        size = len(s)
        rep_of_k = []
        i = 0
        
        stop = lambda idx: idx if idx <= size else size
        
        while i < ( len(s)-k+1 ):
            substr_of_k = s[ i: i+k ]
            
            if len(set(substr_of_k)) == 1 and substr_of_k == substr_of_k[::-1] :
                
                rep_of_k.append( substr_of_k )
                i += k
            else:
                i += 1
            
        return rep_of_k
    
    def removeDuplicates(self, s: str, k: int) -> str:
        
        rep_of_k = self.helper(s, k)
        
        while len(rep_of_k) != 0:
            
            #print( "rep of k", rep_of_k)
            
            for rep in rep_of_k:
                
                s = s.replace( rep, '')
            
            
            # try next run
            rep_of_k = self.helper(s, k)
        
        return s