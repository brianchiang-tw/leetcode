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



from collections import Counter
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # key   : number
        # value : occurrence
        
        num_occ_dict_1 = Counter(nums1)
        num_occ_dict_2 = Counter(nums2)
        
        # list for intersection output
        list_of_intersection = []
        
        # create list of intersection based on occurrence of number
        # select the dictionary which is the shorter one.
        if len(num_occ_dict_1) <= len(num_occ_dict_2):
            for num_as_key in num_occ_dict_1:
                list_of_intersection.extend( [num_as_key] * min( num_occ_dict_1[num_as_key], num_occ_dict_2[num_as_key] ) )
                
        else:
            for num_as_key in num_occ_dict_2:
                list_of_intersection.extend( [num_as_key] * min( num_occ_dict_1[num_as_key], num_occ_dict_2[num_as_key] ) )
            
            
        return list_of_intersection



# m : length of nums1
# n : length of nums2


## Time Complexity: O( m + n )
#
# The overhead in time is the Counter building, which is of O( m + n )

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for Counter, which is of O( m + n )



def test_bench():

    test_data = [
                    ([1,2,2,1], [2,2]),
                    ([4,9,5], [9,4,9,8,4])
                ]

    # expected output:
    '''
    [2, 2]
    [4, 9]
    '''

    for arr1, arr2 in test_data:

        print( Solution().intersect(arr1, arr2) )
    
    return 



if __name__ == '__main__':

    test_bench()