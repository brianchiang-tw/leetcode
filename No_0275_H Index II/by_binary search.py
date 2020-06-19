'''

Description:

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?

'''



from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left, right = 0, len(citations)-1
        
        size = len(citations)
        
        while left <= right:
            
            mid = left + (right - left)//2
            
            the_number_of_larger_equal_to_current = size - mid
            h_index = citations[mid]
            
            
            if h_index < the_number_of_larger_equal_to_current:
                # current h index is too small, make it larger
                left = mid + 1
                    
            elif h_index > the_number_of_larger_equal_to_current:
                # current h index is to large, make it smaller
                right = mid - 1
            
            else:
                # meet the definition of h-index
                return h_index
            
        return size - left 



# n : the length of input list, citations

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        h_index = Solution().hIndex( citations = [0,1,3,5,6] )
        self.assertEqual( h_index, 3 )



if __name__ == '__main__':

    unittest.main()