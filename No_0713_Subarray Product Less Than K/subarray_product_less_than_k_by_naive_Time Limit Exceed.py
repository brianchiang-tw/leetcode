from functools import reduce

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        list_of_subarry = []
            
        for i in range(len(nums)):
            
            for j in range(i, len(nums)):
                
                sub_array = nums[i:j+1]
                if reduce( operator.mul, sub_array, 1 ) < k:
                    list_of_subarry.append( sub_array )
                
        
        return len(list_of_subarry)