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
        
        def helper( nums, left, right, target):
            
            if left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid
                
                if nums[mid] < nums[right]:
                    # right part is kept sorted in ascending order after rotation
                    
                    if nums[mid] < target <= nums[right]:
                        return helper( nums, mid+1, right, target)
                    else:
                        return helper( nums, left, mid-1, target)
                
                else:
                    # left part is sorted kept in ascending order after rotation
                    
                    if nums[left] <= target < nums[mid]:
                        return helper( nums, left, mid-1, target)
                    else:
                        return helper( nums, mid+1, right, target)
                    
            
            else:
                return -1
        # -------------------------------------------------------------
        return helper( nums, left = 0, right = len(nums)-1, target = target)




# n : the length of input array, nums.

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n ).

## Space Complexity: O( log n )
#
# The overhead in space is depth of recursion stack, which is of O( log n ).



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