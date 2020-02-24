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
            top = heappop(heap)
            
            # update lookup table
            Solution.table.append(top)
            
            # Remove repeated ugly number
            while len(heap)!= 0 and heap[0] == top:
                top = heappop(heap)
            
            # Next element = minimal ugly number x 2, x 3, x 5
            heappush(heap, top*2)
            heappush(heap, top*3)
            heappush(heap, top*5)
        
        # update lookup table
        Solution.table.append(heap[0])
    
    
    
    def nthUglyNumber(self, n: int) -> int:
        
        if not Solution.table:
            ## Initialization:
            # Build once, for quick resonse to query everytime.
            self.build_look_up_table()
        
        return Solution.table[n-1]



# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the cost of heap building, which is of O( n ).

## Space Complexity: O( n )
#
# The voerhead in space is the storage for the heap, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'n')
def test_bench():

    test_data = [
                    TestEntry( n = 1),
                    TestEntry( n = 2),
                    TestEntry( n = 3),
                    TestEntry( n = 4),
                    TestEntry( n = 5),
                    TestEntry( n = 10),
                    TestEntry( n = 100),
                    TestEntry( n = 1000),
                    TestEntry( n = 1500),
                    TestEntry( n = 1690)
                ]

    # expected output:
    '''
    1
    2
    3
    4
    5
    12
    1536
    51200000
    859963392
    2123366400
    '''

    calculator = Solution()
    for t in test_data:
        print( calculator.nthUglyNumber( n = t.n ) )

    return 



if __name__ == '__main__':

    test_bench()
