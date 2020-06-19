'''

Description:

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.

'''



from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort( reverse = True )
        
        for idx, citation in enumerate(citations):

            # find the first index where citation is smaller than array index            
            if idx >= citation:
                return idx
        
        return len(citations)



# n : the length of input list, recitations

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        h_index = Solution().hIndex( [3,0,6,1,5] )
        self.assertEqual( h_index, 3)



    def test_case_2(self):

        h_index = Solution().hIndex( [1,2,3,4,5] )
        self.assertEqual( h_index, 3)



    def test_case_3(self):

        h_index = Solution().hIndex( [1,2,1,1,2] )
        self.assertEqual( h_index, 2)


    def test_case_4(self):

        h_index = Solution().hIndex( [99, 100] )
        self.assertEqual( h_index, 2)



if __name__ == '__main__':

    unittest.main()