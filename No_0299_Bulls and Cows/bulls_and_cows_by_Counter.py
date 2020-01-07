from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        secret_list, guess_list = list(secret), list(guess)
        
        i = 0
        
        while i < len(secret_list):
            
            if secret_list[i] == guess_list[i]:
                
                del secret_list[i], guess_list[i]
                
                i -= 1
                
            i += 1
            
        
        num_of_A = len(secret)-len(secret_list)
        num_of_B = sum( ( Counter(secret_list) & Counter(guess_list) ).values() )
        
        return str(num_of_A) + "A" + str(num_of_B) + "B"