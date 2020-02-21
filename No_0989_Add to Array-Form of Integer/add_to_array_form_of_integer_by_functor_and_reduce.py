'''

Description:

For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

 

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
 

Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0

'''



from functools import reduce
from typing import List
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        digit_to_int = lambda x, y: 10*x+y

        return list( map( int, str( reduce( digit_to_int, A) + K ) ) )



# a : the integer value of input digit list A
# k : the value of input K

## Time Complexity: O( a + k )
#
# The overhead in time is the string<->integer conversion, 
# as well as integer addition, which are of O( a + k )

## Space Complexity: O( a + k )
#
# The overhead in space is the storage for output list, which is of O( a + k )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence_A k')
def test_bench():

    test_data = [
                    TestEntry(sequence_A = [1,2,0,0], k = 34),
                    TestEntry(sequence_A = [2,7,4], k = 181),
                    TestEntry(sequence_A = [2,1,5], k = 806),
                    TestEntry(sequence_A = [9,9,9,9,9,9,9,9,9,9], k = 1 ),
                ]

    # expected output:
    '''
    [1, 2, 3, 4]
    [4, 5, 5]
    [1, 0, 2, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    '''


    for t in test_data:

        print( Solution().addToArrayForm(t.sequence_A, t.k) )
    
    return 



if __name__ == '__main__':

    test_bench()