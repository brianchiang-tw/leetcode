'''

Description:

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''


from typing import List
class Solution:
    
    def first_occ_bst(self, nums: List[int], target: int)->int:
        
        size = len(nums)
        left, right = 0, size
        
        while left < right:
            
            mid = ( left + right ) // 2
            mid_value = nums[ mid ]
            
            # make right bound as tight as possible
            if mid_value >= target:
                right = mid
            else:
                left = mid+1
                
                
        if left == size or nums[left] != target:
            return -1
        else:
            return left

        
        
    def last_occ_bst(self, nums: List[int], target: int)->int:
        
        size = len(nums)
        left, right = 0, size
        
        while left < right:
            
            mid = ( left + right ) // 2
            mid_value = nums[ mid ]
            
            # make left bound as tight as possible
            if mid_value > target:
                right = mid
            else:
                left = mid+1
        
        # left points to next number larger than target
        # thus minus 1 to the tail index of target
        left -= 1
        if left < 0 or nums[left] != target:
            return -1
        else:
            return left
        
        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = self.first_occ_bst( nums, target)
        last  = self.last_occ_bst( nums, target)
        return [first, last]



# n : the length of input nums

## Time Complexity: O( log n )
#
# The major overhead in time is the while loop for varint binary search, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The major overhead in space is storage for variables in variant binary search, which is of O( 1 )



def test_bench():

    test_data = [
                    ( [5,7,7,8,8,10], 8 ),
                    ( [5,7,7,8,8,10], 6 ),
                    ( [3,3,3], 3 ),
                    ( [1,3], 1 ),
                    ( [2,2], 2 )
                ]

    # expected output:
    '''
    [3, 4]
    [-1, -1]
    [0, 2]
    [0, 0]
    [0, 1]
    '''


    for test_pair in test_data:

        print( Solution().searchRange(*test_pair) )

    return 



if __name__ == '__main__':

    test_bench()