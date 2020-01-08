''''

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
        
        even_part   = ( x for x in A if x%2 == 0 )
        odd_part    = ( x for x in A if x%2 == 1 )
        
        return list(even_part) + list(odd_part)


# n : the length of input list, A.

## Time Complexity: O( n )
#
# The overhead in time is the two-pass generator, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the list of two generators, which is of O( n ).




def test_bench():

    test_data = [ 1, 2, 5, 4, 3, 6, 8, 9, 7, 10]

    # expected output:
    '''
    [2, 4, 6, 8, 10, 1, 5, 3, 9, 7]
    '''


    print( Solution().sortArrayByParity(test_data ) )

    return 



if __name__ == '__main__':

    test_bench()
