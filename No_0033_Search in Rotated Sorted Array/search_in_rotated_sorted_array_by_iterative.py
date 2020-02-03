'''

Description:


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4



Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''



from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper_binary_search( nums, start, end, target):
            
            while start <= end:
            
                mid = start + (end-start)//2

                if nums[mid] == target:
                    # base case:
                    # hit
                    return mid

                # Divide-and-conquer
                if nums[mid] < nums[end]:
                    # right half keeps sorted in ascending order after rotation


                    if nums[end] >= target > nums[mid]:
                        # search target in right half
                        start = mid+1

                    else:
                        # search target in left half
                        end = mid-1

                else:
                    # left half keeps sorted in ascending order after rotation

                    if nums[start] <= target < nums[mid]:
                        # search target in left half
                        end = mid-1

                    else:
                        # search target in right half
                        start = mid+1


            # base case:
            # miss
            # target does not exist in the list
            return -1
            
            
        return helper_binary_search(nums, 0, len(nums)-1, target)



# n : the length of input array, nums.

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the looping variable and index variable, which is of O( 1 ).



def test_bench():

    test_data = [
                    ([4,5,6,7,0,1,2], 0),
                    ([4,5,6,7,0,1,2], 3)
                ]

    # expected output:
    '''
    4
    -1
    '''

    for sequence, target in test_data:

        print( Solution().search( nums=sequence, target = target ) )
    
    return 



if __name__ == '__main__':

    test_bench()