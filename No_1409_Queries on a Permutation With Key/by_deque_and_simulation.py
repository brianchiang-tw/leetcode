'''

Description:

Given the array queries of positive integers between 1 and m, you have to process all queries[i] (from i=0 to i=queries.length-1) according to the following rules:

In the beginning, you have the permutation P=[1,2,3,...,m].
For the current i, find the position of queries[i] in the permutation P (indexing from 0) and then move this at the beginning of the permutation P. Notice that the position of queries[i] in P is the result for queries[i].
Return an array containing the result for the given queries.

 

Example 1:

Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1] 
Explanation: The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5]. 
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5]. 
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5]. 
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5]. 
Therefore, the array containing the result is [2,1,2,1].  



Example 2:

Input: queries = [4,1,2,2], m = 4
Output: [3,1,2,0]



Example 3:

Input: queries = [7,5,5,8,3], m = 8
Output: [6,5,0,7,5]
 

Constraints:

1 <= m <= 10^3
1 <= queries.length <= m
1 <= queries[i] <= m

'''



from collections import deque
from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        # a sequence of number, from 1 to m
        sequence = deque( [ *range(1,m+1) ] )
        
        # index record of query number
        index_record = []
        
        for q in queries:
            
            # record index of query number
            index_record.append( sequence.index(q) )
            
            # relocate query number from original position to head position
            sequence.remove(q)
            sequence.appendleft(q)
            
        return index_record



# m : the value of input parmeter m.
# n : the length of input list, queries

## Time Complexity: O( m*n )
#
# The overhead in time is the cost of loop, which is of O( n ),
# and the cost of indexing and removal, which is of O( m )
#
# It takes O( m * n ) in total.

## Space Complexity: O( n )
#
# The overhead in space is the storagefor output list, index_record, which is of O( n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'queries m')
def test_bench():

    test_data = [
                    TestEntry( queries = [3,1,2,1], m = 5 ),
                    TestEntry( queries = [4,1,2,2], m = 4 ),
                    TestEntry( queries = [7,5,5,8,3], m = 8 ),
                ]


    # expected output:
    '''
    [2, 1, 2, 1]
    [3, 1, 2, 0]
    [6, 5, 0, 7, 5]
    '''

    for t in test_data:

        print( Solution().processQueries( queries=t.queries, m = t.m ) )

    return


if __name__== '__main__':

    test_bench()                