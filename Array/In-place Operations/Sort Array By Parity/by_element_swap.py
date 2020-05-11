'''

Description:

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

'''



from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        
        even_position = 0
        
        #for idx, number in enumerate(A):
        for idx in range(len(A)):
            
            if A[idx] & 1 == 0:
                A[idx], A[even_position] = A[even_position], A[idx]
                even_position += 1
        
        return A



# n : the length of input list, A

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [3,1,2,4] ),
                    TestEntry( sequence = [2,1,6,3] ),
                    TestEntry( sequence = [1,2,3,4,5] ),
                ]

    # expected output:
    '''
    [2, 4, 3, 1]
    [2, 6, 1, 3]
    [2, 4, 3, 1, 5]
    '''

    for t in test_data:

        print( Solution().sortArrayByParity( A = t.sequence ) )
    
    return



if __name__ == '__main__':

    test_bench()    