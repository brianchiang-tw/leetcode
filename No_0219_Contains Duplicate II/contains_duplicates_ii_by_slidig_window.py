'''

Description:

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == len( set(nums) ):
            # Reject array with distinct element
            return False
        
        
        
        for i, cur_value in enumerate(nums):
            
            # Sliding window from i+1 to i+k
            for j in range( i+1, i+k+1, 1):

                if j >= len(nums):
                    continue

                else:
                    if nums[j] == cur_value:
                        return True

        return False


# n : the length of input array
# k : the distance upper bound

## Time Complexity: O( nk ) = O( n )
#
# The overhead in time is the double for loop on sliding windows, which is of O( n*k )

## Space Complexity: O( n )
#
# The major overhead in space is the storage for set, which is of O( n )


def test_bench():

    test_data = [
                        ( [1,2,3,1], 3 ),
                        ( [1,0,1,1], 1 ),
                        ( [1,2,3,1,2,3], 2 )
                ]


    # expected output:
    '''
    True
    True
    False
    '''

    for test_pair in test_data:

        print( Solution().containsNearbyDuplicate(*test_pair) )

    return



if __name__ == '__main__':

    test_bench()