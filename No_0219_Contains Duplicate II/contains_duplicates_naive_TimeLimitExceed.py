

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
    
        for i, cur_value in enumerate(nums):

            for j in range( i+1, i+k+1, 1):

                if j < 0 or j >= len(nums):
                    continue

                else:
                    if nums[j] == cur_value and j != i:
                        print('j', j)
                        print('cur_value', cur_value)
                        return True

        return False
