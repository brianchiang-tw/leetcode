'''

Descption:

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''


from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        num_occ_dict = Counter(nums)
        
        # description guanatees that majority always exist for every test input.
        # Therefore, we can pick the one with highest occureence as majority element.
        
        return max( num_occ_dict, key = lambda k:num_occ_dict[k] )


# n : the length of input array nums

## Time Complexity: O( n )
#
# The overhead in time is the dictionary building and maximal finding, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, num_occ_dict.



def test_bench():

    test_data = [
                    [3,2,3],
                    [2,2,1,1,1,2,2]
                ]

    # expected output:
    '''
    3
    2
    '''

    for test_array in test_data:

        print( Solution().majorityElement(test_array) )

    return 



if __name__ == '__main__':

    test_bench()