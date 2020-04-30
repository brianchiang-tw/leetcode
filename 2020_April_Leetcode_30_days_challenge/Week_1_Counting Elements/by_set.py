'''

Description:

Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

 

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.



Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.



Example 3:

Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.



Example 4:

Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.
 

Constraints:

1 <= arr.length <= 1000
0 <= arr[i] <= 1000

'''


from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:

        unique_element = set(arr)

        return sum( 1 for elem in arr if (elem+1) in unique_element )



# n : the length of input list, arr.

## Time Complexity: O( n )
#
# The overhead in time is the cost of set creation, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for set, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array')



def test_bench():

    test_data = [
                    TestEntry( array = [1,2,3] ),
                    TestEntry( array = [1,1,3,3,5,5,7,7] ),
                    TestEntry( array = [1,3,2,3,5,0] ),
                    TestEntry( array = [1,1,2,2] ),
                ]


    # expected output:
    '''
    2
    0
    3
    2
    '''

    for t in test_data:

        print( Solution().countElements( arr = t.array ) )
    
    return



if __name__ == '__main__':

    test_bench()    