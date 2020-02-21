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



from operator import add
from functools import reduce

class Solution:
    def intersect(self, nums1, nums2):
        
        if not nums1 or not nums2:
            return []
        
        a, b = map(set, (nums1, nums2))
        
        common_elements = a & b
        
        if not common_elements:
            return []
        
        common_element_occ = [ [element] * min(nums1.count(element), nums2.count(element) ) for element in common_elements ]
        

        return reduce( add, common_element_occ)





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