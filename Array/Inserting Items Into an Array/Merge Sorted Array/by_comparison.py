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



Hint #1  

You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?



Hint #2  

If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.

'''



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



# m : value of input parameter, m
# n : value of input parameter, n

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of while loop, which is of O( m + n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )



def test_bench():

    test_data = [
                    ( [1,2,3,0,0,0], 3, [2,5,6], 3),
                    ( [7,8,9,0,0,0], 3, [2,5,6], 3),
                    ( [1,3,4,0,0,0], 3, [2,5,6], 3),
                    ( [8,9,10,0,0,0], 3, [2,5,6], 3),
                ]

    # expected output:
    '''
    [1, 2, 2, 3, 5, 6]
    [2, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6]
    [2, 5, 6, 8, 9, 10]
    '''

    for t in test_data:

        Solution().merge( *t )

        print( t[0] )
    
    return



if __name__ == '__main__':

    test_bench()