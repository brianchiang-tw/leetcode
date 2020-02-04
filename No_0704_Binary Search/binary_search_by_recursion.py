'''

Description:


Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4



Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].

'''



from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums, left, right, target ):
            
            if left > right:
                # base case:
                # miss
                # target does not exist in input array
                return -1
            
            # update index of mid point
            mid = left + (right-left)//2

            if nums[mid] == target:

                # base case:
                # hit
                return mid

            if target > nums[mid]:
                
                # search target in right half
                return binary_search(nums, mid+1, right, target)

            else:

                # search target in left half
                return binary_search(nums, left, mid-1, target)
        
        
        
        return binary_search(nums, 0, len(nums)-1, target)



# n : the length of input array, nums

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n )

## Spae complexity: O( log n )
#
# The overhead in space is the storage for call stack, which is of O( log n )



def test_bench():

    test_data = [
                    ([-1,0,3,5,9,12], 9),
                    ([-1,0,3,5,9,12], 2)
                ]

    for sorted_sequence, target in test_data:

        print( Solution().search(sorted_sequence, target) )

    return 



if __name__ == '__main__':

    test_bench()