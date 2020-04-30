'''

Description:

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

'''



from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        if len(nums) <= 3:
            # Quick response for small case
            try:
                return nums.index( target )
            except:
                return -1

        # Adaptive binary search            
        left, right = 0, len(nums)-1
        
        while left <= right:
            
            mid = left + (right-left)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[right]:
                # right part is kept sorted in ascending order after rotation

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
            else:
                # left part is kept sorted in ascending order after rotation

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1




# n : the length of input array, nums.

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the looping variable and index variable, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array target')
def test_bench():

    test_data = [
                    TestEntry( array = [4,5,6,7,0,1,2], target = 0),
                    TestEntry( array = [4,5,6,7,0,1,2], target = 3),
                ]

    # expected output:
    '''
    4
    -1
    '''

    for array, target in test_data:

        print( Solution().search( nums=array, target = target ) )
    
    return 



if __name__ == '__main__':

    test_bench()