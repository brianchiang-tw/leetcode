'''

Description:

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

'''

from collections import defaultdict
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        # key: element value
        # value: index of element in nums2
        elem_index_dict = defaultdict(int)
        
        
        # create key, value pair from nums2
        for i, elem in enumerate( nums2 ):
            elem_index_dict[elem] = i
        
        
        next_greater = []
        
        # visit each x in nums1, try to find next great element in nums2
        for x in nums1:
            
            for j in range( elem_index_dict[x]+1, len(nums2) ):
                
                y = nums2[j]
                if y > x:
                    next_greater.append( y )
                    break
            else:
                next_greater.append(-1)
                            
        return next_greater


# N : number of elements in input nums2

## Time Complexity: O( N )
#
# The overhead in time is the nested for loop on nums1 and nums2
# It takes O( N^2 ) at most.

## Space Complexity: O( N )
#
# The overhead in space is to maintain a dictionary and output list
# Both of them take O( N )


def test_bench():

    test_data = [ 
                    ( [4,1,2], [1,3,4,2] ),
                    ( [2,4], [1,2,3,4] )
                ]


    # expected output:
    '''
    [-1, 3, -1]
    [3, -1]
    '''


    for test_pair in test_data:

        next_greater_element = Solution().nextGreaterElement( *test_pair)

        print( next_greater_element )

    return



if __name__ == '__main__':

    test_bench()