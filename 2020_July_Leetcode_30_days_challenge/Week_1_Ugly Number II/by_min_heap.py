'''

Description:

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12

Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

'''



from heapq import heappush, heappop

class Solution:
    
    # lookup table to speed up query response time
    table = []
    
    def build_look_up_table(self):
    
        heap = [1]
        upper_bound = 1690
        
        for i in range(upper_bound):
            
            # Get minimal element
            min_u = heappop(heap)
            
            # update lookup table
            Solution.table.append(min_u)
            
            # Remove repeated ugly number
            while len(heap)!= 0 and heap[0] == min_u:
                min_u = heappop(heap)
            
            # Next generation of u-family = minimal ugly number x 2, x 3, x 5
            heappush(heap, min_u*2)
            heappush(heap, min_u*3)
            heappush(heap, min_u*5)
        
        # update lookup table
        Solution.table.append(heap[0])
    
    
    
    def nthUglyNumber(self, n: int) -> int:
        
        if not Solution.table:
            ## Initialization:
            # Build once, for quick resonse to query everytime.
            self.build_look_up_table()
        
        return Solution.table[n-1]



# n : the value of input

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of min-heap maintainance, which is of O( n log n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for min-heap, which is of O( n ).


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().nthUglyNumber(10)
        self.assertEqual(result, 12)


    def test_case_2(self):

        result = Solution().nthUglyNumber(1)
        self.assertEqual(result, 1)


    def test_case_3(self):

        result = Solution().nthUglyNumber(2)
        self.assertEqual(result, 2)


    def test_case_3(self):

        result = Solution().nthUglyNumber(3)
        self.assertEqual(result, 3)



if __name__ == '__main__':

    unittest.main()