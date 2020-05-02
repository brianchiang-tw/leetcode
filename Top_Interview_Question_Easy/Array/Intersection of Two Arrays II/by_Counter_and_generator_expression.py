'''

Description:

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]



Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''



from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
		# build number-occurence dictionary for nums1 and nums2
        num_occ_dict_1, num_occ_dict_2 = map( Counter, [ nums1, nums2 ] )
       
	    # compute intersection
        intersection = num_occ_dict_1 & num_occ_dict_2
        
		# output intersection element with corresponding occurrences
        return sum( ( [num]*occ for num, occ in intersection.items() ), [] )



# m : length of nums1
# n : length of nums2


## Time Complexity: O( m + n )
#
# The overhead in time is the set building, which is of O( m + n )

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for set, which is of O( m + n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'nums1 nums2')
def test_bench():

    test_data = [
                    TestEntry( nums1 = [1,2,2,1], nums2 = [2,2] ),
                    TestEntry( nums1 = [4,9,5]  , nums2 = [9,4,9,8,4])
                ]

    # expected output:
    '''
    [2, 2]
    [4, 9]
    '''

    for t in test_data:

        print( Solution().intersect(t.nums1, t.nums2) )
    
    return 



if __name__ == '__main__':

    test_bench()        