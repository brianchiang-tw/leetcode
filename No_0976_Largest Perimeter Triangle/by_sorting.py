'''

Description:

Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

 

Example 1:

Input: [2,1,2]
Output: 5



Example 2:

Input: [1,2,1]
Output: 0



Example 3:

Input: [3,2,3,4]
Output: 10



Example 4:

Input: [3,6,2,3]
Output: 8
 

Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6

'''



from typing import List
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
		# sort side length in descending order
        A.sort( reverse = True )
        
		# Try and test from largest side length
        for i in range( len(A) - 2):
            
            if A[i] < A[i+1] + A[i+2]:
                # Early return when we find largest perimeter triangle
                return A[i] + A[i+1] + A[i+2]
        
        # Reject: impossible to make triangle
        return 0



# n : the length of input list, A

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n)

## Space Complexity: O( 1 )
#
# The overhead in space is the cost of temporarily variable and loop index, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'side_length')
def test_bench():

    test_data = [
                    TestEntry( side_length = [2,1,2] ),
                    TestEntry( side_length = [1,2,1] ),
                    TestEntry( side_length = [3,2,3,4] ),
                    TestEntry( side_length = [3,6,2,3] ),
                ]

    # expected output:
    '''
    5
    0
    10
    8
    '''

    for t in test_data:

        print( Solution().largestPerimeter( A = t.side_length ) )                
    
    return 



if __name__ == '__main__':

    test_bench()