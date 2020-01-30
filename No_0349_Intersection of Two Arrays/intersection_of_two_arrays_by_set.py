'''

Description:

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

'''



from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # set of first list, nums1
        set_1 = set(nums1)
        
        # set of second list, nums2
        set_2 = set(nums2)
        
        # intersection of these two sets
        return list( set_1 & set_2 )



# m : length of nums1
# n : length of nums2

## Time Complexity: O( m + n )
#
# The overhead in time is set operation over nums1 and nums2, which is of O( m + n ).


## Space Complexity: O( m + n )
#
# The overhead in space is the storage for set_1 and set_2, which is of O( m + n ).


def test_bench():

    test_data = [ 
                    ([1,2,2,1], [2,2]),
                    ([4,9,5], [9,4,9,8,4]),
                    ([1,3,5], [2,3,4,5])
                ]
    
    # expected output:
    '''
    [2]
    [9, 4]
    [3, 5]    
    '''


    for arr1, arr2 in test_data:

        print( Solution().intersection(arr1, arr2) )
    
    return 



if __name__ == '__main__':

    test_bench()