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
        
        a = nums1[:m]
        b = nums2
        
        pos = 0
        
        while a and b:
            
            if a[0] < b[0]:
                nums1[pos] = a.pop(0)
                
            else:
                nums1[pos] = b.pop(0)
        
            pos += 1
            
        
        while a:
            nums1[pos] = a.pop(0)
            pos += 1
            
        while b:
            nums1[pos] = b.pop(0)
            pos += 1
            
			
        return


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