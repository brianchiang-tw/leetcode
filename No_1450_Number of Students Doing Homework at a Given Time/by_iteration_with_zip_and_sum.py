'''

Description:

Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

 

Example 1:

Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.



Example 2:

Input: startTime = [4], endTime = [4], queryTime = 4
Output: 1
Explanation: The only student was doing their homework at the queryTime.



Example 3:

Input: startTime = [4], endTime = [4], queryTime = 5
Output: 0



Example 4:

Input: startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
Output: 0



Example 5:

Input: startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5
Output: 5
 

Constraints:

startTime.length == endTime.length
1 <= startTime.length <= 100
1 <= startTime[i] <= endTime[i] <= 1000
1 <= queryTime <= 1000

'''



from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        homework_interval = zip(startTime, endTime)
        
        return sum( ( start <= queryTime <= end ) for start, end in homework_interval )



# n : the total number of students

## Time Complexity: O( n )
#
# The overhead in time is the cost of generator expression and summation, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary iterator and generator, which is of O( 1 ).

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'start_t end_t query_t')


def test_bench():

    test_data = [
                    TestEntry( start_t = [1,2,3], end_t = [3,2,7], query_t = 4 ),
                    TestEntry( start_t = [4], end_t = [4], query_t = 4 ),
                    TestEntry( start_t = [4], end_t = [4], query_t = 5 ),
                    TestEntry( start_t = [1,1,1,1], end_t = [1,3,2,4], query_t = 7 ),
                    TestEntry( start_t = [9,8,7,6,5,4,3,2,1], end_t = [10,10,10,10,10,10,10,10,10], query_t = 5 ),
                ]

    # expected output:
    '''
    1
    1
    0
    0
    5
    '''

    for t in test_data:
        print( Solution().busyStudent( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()