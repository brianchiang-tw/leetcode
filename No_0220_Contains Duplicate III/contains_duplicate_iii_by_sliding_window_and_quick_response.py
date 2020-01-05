'''

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

'''


from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        size = len(nums)
        
        diff_sum = 0

        if t == 0 and len(nums) == len( set(nums) ):
            # Quick response for special case on t = 0
            # t = 0 requires at last one pair of duplicate elements
            return False
        
        
        
        for i, cur_val in enumerate(nums):
            
            for j in range( i+1, i+k+1):
                
                if j >= size:
                    # avoid index out of boundary
                    break
                
                if abs(cur_val - nums[j]  ) <= t:
                    # hit: 
                    # i != j, | i-j | <= k
                    # | nums[i] - nums[j] | <= t
                    return True
                
            
        return False



# n : the length of input array, nums.
# k : the distance upper bound

## Time Complexity: O( n*k )
#
# The overhead in time is the nested for loops iterating on (i, cur_val), and j, which are of O( n * k )

## Space Complexity: O( n )
#
# The major overhead in space is the storage for the set of nums, which is of O( n ).



def test_bench():

    test_data = [
                    ( [1,2,3,1], 3, 0 ),
                    ( [1,0,1,1], 1, 2 ),
                    ( [1,5,9,1,5,9], 2, 3 ),
                    ( [3,6,0,4], 2, 2 ),
                    ( [range(1,10000)], 2, 0 )
                ]

    # expected output:
    '''
    True
    True
    False
    True
    False
    '''


    for nums, k ,t in test_data:

        print( Solution().containsNearbyAlmostDuplicate(nums, k ,t) )

    return 



if __name__ == '__main__':

    test_bench()
