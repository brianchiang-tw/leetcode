'''

Description:

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

'''

# Python feature: type hint
from typing import List

# for python built-in library, bisect   
import bisect
class Solution:

    def _merge( self, left_part, right_part ):


        merge_list = sorted( left_part + right_part )

        return merge_list


    def merge_sort_with_rev_pair_count( self, nums: List[int]) -> (List[int], int):
        

        
        if len( nums) <= 1:
        # Base case:

            return nums, 0

        else:
        # General case
            mid = len(nums) // 2

            # Divide-and-conquer with the merge-sort framework

            # Divide:
            left_part, left_rev_pair_count = self.merge_sort_with_rev_pair_count( nums[ : mid] )
            right_part, right_rev_pair_count = self.merge_sort_with_rev_pair_count( nums[ mid: ] )


            # Conquer:
            # collect the reverse pair count from left part and right part
            rev_pair_count = left_rev_pair_count + right_rev_pair_count

            cur_rev_pair_count = 0

            for r in right_part:
                
                # for every r in right_part, calculate the reverse pairs
                cur_rev_pair_count = len( left_part ) - bisect.bisect( left_part, 2*r)

                # if there exist one r has no reverse pairs,
                # then any r' after r must have no reverse pairs, either.
                if cur_rev_pair_count == 0:
                    break

                # update total reverse pair count from current reverse pair count
                rev_pair_count += cur_rev_pair_count

            # Conquer:
            # Merge left_part and right into a sorted list with ascending order
            merged_list = self._merge( left_part, right_part)

        return merged_list, rev_pair_count



    def is_strictly_increasing_by_one( self, nums :List[int]) -> bool:

        result = all( ( i < j and (j-1) == 1 ) for i, j in zip(nums, nums[1:]) ) 

        return result


    def reversePairs( self, nums: List[int]) -> int:

        # corner case handling
        if self.is_strictly_increasing_by_one( nums ) or len(nums) <= 1:
            return 0

        sorted_list, count_of_reverse_pair = self.merge_sort_with_rev_pair_count( nums )

        return count_of_reverse_pair


# N : the length of input list, nums.

## Time Complexity : O( N * log(N) )
#
# This implemention of reverse pair counting is based on merge sort.
# Divide stage takes O( log(N) ) to split sub-problem till base case.
# Thus the depth of recusion tree is O( log(N) )

# And, conquer stage takes O( N ) to merge left part and right part, and collect reverse pairs
# Therefore, the loading per level is O( N )

# In summary, whole procedure takes O( N * log(N) ) to compute the number of reverse pairs

## Space Complexity : O( N )
#
# In each recusion call, we need some variable for left_part, left_rev_pair_count, right_part, right_rev_pair_count, 
# rev_pair_count, merged_list.
# The overhead is at most O( N )

def test_bench():

    test_data = [ 
                    [1,3,2,3,1],
                    [2,4,3,5,1],
                    [1,3,2,3,1],
                    [*range(5, 0, -1)],
                    [*range(1,6,1)],
                    [-7, -4]
                ]
    
    # expected output:
    '''
    2
    3
    2  
    4
    0
    1
    ''' 


    for test in test_data:

        len_of_rev_pair = Solution().reversePairs( test )

        print( len_of_rev_pair  )


    return



if __name__ == '__main__':

    test_bench()