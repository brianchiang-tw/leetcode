from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        num_occ_dict = Counter( nums )
        
        num_occ_pair = num_occ_dict.items()
        max_occ = max( list( num_occ_dict.values() ) )
        
        #print("max_occ", max_occ )
        
        candidate_num = []
        
        for num, occ in num_occ_dict.items():
            
            if occ == max_occ:
                candidate_num.append( num )
                
                
        min_len_of_same_degree = len(nums)
            
        for x in candidate_num:
            
            min_pos = len(nums)
            max_pos = 0
            for index,y in enumerate(nums):
                
                if y == x:
                    min_pos = min( min_pos, index)
                    max_pos = max( max_pos, index)
            
            #print( min_pos )
            #print( max_pos )
            min_len_of_same_degree = min( min_len_of_same_degree, max_pos - min_pos + 1)
            
        return min_len_of_same_degree