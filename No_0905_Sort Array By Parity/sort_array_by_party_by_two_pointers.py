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
        
        i, j = 0, len(A)-1
        
        while i < j:
            
            if A[i]%2==1 and A[j]%2 == 0: 
                A[i], A[j] = A[j], A[i]
            
            i , j = i+1-A[i]%2 , j-A[j]%2
        
        return A


# n : the length of input list, A.

## Time Complexity: O( n )
#
# The overhead in time is the while loop, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the loop variable and index, which is of O( 1 ).




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
