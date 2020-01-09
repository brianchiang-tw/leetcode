'''

Description:

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

'''


from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        # sorting input list with absolute value on ascending order
        A.sort( key = abs )
        

        # generate square value by list comprehension
        return [ x**2 for x in A ]



# n : the length of input list, A.

## Time Complexity : O( n log n ) on average, O( n ^ 2 ) on worst case.
#
# The overhead in time is the pre-processing of soring, which is of O( n log n ) on average, O( n ^ 2) on worst case.

## Space Complexity : O( n )
#
# The overhead in space is the storage for the list comprehension of square values, which is of O( n ).



def test_bench():

    test_data = [
                    [-4,-1,0,3,10],
                    [-7,-3,2,3,11]
                ]

    # expected output:
    '''
    [0, 1, 9, 16, 100]
    [4, 9, 9, 49, 121]
    '''



    for sequence in test_data :

        print( list( Solution().sortedSquares(sequence) ) )
    
    return 



if __name__ == '__main__':

    test_bench()