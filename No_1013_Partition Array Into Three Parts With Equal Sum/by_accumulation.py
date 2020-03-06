Implementation:

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        
        
        sum_of_A = sum(A)
        
        if sum_of_A % 3 != 0:
            
            return False
        
        else:
            target = sum_of_A // 3

            size = len(A)
            accumulation, partition = 0, 0

            for idx,number in enumerate(A):

                accumulation += number
                
                if partition == 0:
                    if accumulation == target:
                        # We find first chunk of 1/3
                        partition = 1
                        
                        
                elif partition == 1:
                    if accumulation == 2*target and idx != (size-1):
                        # We find second chunk of 1/3 in the middle
                        # then the last chink must be 1/3 also.
                        
                        # Therefore, we have 3 chunks of 1/3
                        partition = 3
                        return True
                

            return False