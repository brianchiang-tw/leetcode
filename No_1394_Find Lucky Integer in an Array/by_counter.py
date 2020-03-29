'''

Description:

Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

 

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.



Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.



Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.



Example 4:

Input: arr = [5]
Output: -1



Example 5:

Input: arr = [7,7,7,7,7,7,7]
Output: 7
 

Constraints:

1 <= arr.length <= 500
1 <= arr[i] <= 500

'''



from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
		# key   : number
		# value : occurrence
        num_occ_dict = Counter( arr )
        
		# find the lucky number with highest occurrence
        return max( [num for num, occ in num_occ_dict.items() if num == occ ] + [-1] )




from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [2,2,3,4] ),
                    TestEntry( sequence = [1,2,2,3,3,3] ),
                    TestEntry( sequence = [2,2,2,3,3] ),
                    TestEntry( sequence = [5] ),
                    TestEntry( sequence = [7,7,7,7,7,7,7] ),
                ]


    # expected output:
    '''
    2
    3
    -1
    -1
    7
    '''

    for t in test_data:
        
        print( Solution().findLucky( arr = t.sequence ) )

    return



if __name__ == '__main__':

    test_bench()