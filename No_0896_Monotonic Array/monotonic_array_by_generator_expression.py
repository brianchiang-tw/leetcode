'''

Description:

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true



Example 2:

Input: [6,5,4,4]
Output: true



Example 3:

Input: [1,3,2]
Output: false



Example 4:

Input: [1,2,4,5]
Output: true



Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000


'''



from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        if not A or len(A) < 3 or len(set(A)) == 1:
            # Quick response:
            # If A is empty list, or A has only two numbers, or All of A is unique number,
            # them direct return True
            return True
        
        monotonic_increasing = all( ( A[i] <= A[i+1] for i in range(len(A)-1) ) )

        if monotonic_increasing:
            return True

        monotonic_decreasing = all( ( A[i] >= A[i+1] for i in range(len(A)-1) ) )
        
        if monotonic_decreasing:
            return True
        else:
            return False



# n : the length of input list, A.

## Time Complexity: O( n )
#
# The overhead in time is the iteration on all( ... ) with generator, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is looping index and judgement variables, which is of O( 1 ).




def test_bench():

    test_data = [
                    [1,2,2,3],
                    [6,5,4,4],
                    [1,3,2],
                    [1,2,4,5],
                    [1,1,1]
                ]

    # expected output:
    '''
    True
    True
    False
    True
    True    
    '''

    for sequence in test_data:

        print( Solution().isMonotonic(sequence) )

    return 



if __name__ == '__main__':

    test_bench()