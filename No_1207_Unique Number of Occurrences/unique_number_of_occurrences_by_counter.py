'''

Description:

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

'''


from collections import Counter
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        num_occ_dict = Counter( arr )
        
        occ = num_occ_dict.values()
        
        return len(occ) == len( set(occ) )

# n : length of input list, arr

## Time Complexity: O( n )
#
# Although it may seems to be O( 1 ) at first glimpse,
# actually, it takes O( n ) due to the built-in Counter dictionary structure.

## Space Complexity: O( n )
#
# The overhead in space is to maintain a Counter dictionary, of O( n ), for occurrence statistics.


def test_bench():

    test_data = [
                    [1,2,2,1,1,3],
                    [1,2],
                    [-3,0,1,-3,1,1,1,-3,10,0]
                ]


    # expected output:
    '''
    True
    False
    True
    '''

    for test_seq in test_data:

        print( Solution().uniqueOccurrences(test_seq) )

    return



if __name__ == '__main__':

    test_bench()