'''

Description:

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

'''

# Note:
# Python O( m + n ) sol. based on merge process derived from merge-sort

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        insert_pos = m + n - 1
        
        idx_1, idx_2 = m-1, n-1
        
        # Choose maximal element, move it to the insert position
        while ( idx_1 >= 0 ) and ( idx_2 >= 0 ):
            
            if nums1[ idx_1 ] >= nums2[ idx_2 ]:
                
                nums1[ insert_pos ] = nums1[ idx_1 ]
                idx_1 -= 1
                
            else:
                
                nums1[ insert_pos ] = nums2[ idx_2 ]
                idx_2 -= 1
                
            insert_pos -= 1
        
        # -------------------------------------------------------
        # nums2 is done, directly merge nums1
        # nums1 will be just on the right position
        pass

        # -------------------------------------------------------
        # nums1 is done, directly merge nums2            
        while idx_2 >= 0:
            
            nums1[ insert_pos ] = nums2[ idx_2 ]
            
            idx_2 -= 1
            insert_pos -= 1


# m : length of input nums1
# n : length of input nums2

## Time Complexity: O( m + n )
#
# The overhead in time is the merge process's while loop, which is of O( m + n )

## Space Complexity: O( 1 )
#
# Problem description guarantee that nums1 has enough extra space for n elements.
# Thus, we don't have to allocate new space for merged arrays.
# It is O( 1 )



def test_bench():

    test_data = [ ([1,2,3,0,0,0], [2,5,6]) ]

    # expected output:
    '''
    [1, 2, 2, 3, 5, 6]
    '''

    for test_pair in test_data:

        nums1, nums2 = test_pair

        Solution().merge( nums1, 3, nums2, 3)

        print( nums1 )

    return 



if __name__ == '__main__':

    test_bench()