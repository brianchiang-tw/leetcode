'''

Description:

Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]



Example 2:

Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
Example 3:

Input: nums = [1], index = [0]
Output: [1]
 

Constraints:

1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i

'''



from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        output = []
        
        for idx, number in zip( index, nums):
            output.insert( idx, number)
            
        return output



# n : the length of input list, numbers.

## Time Complexity: O ( n^2 )
#
# The overhead in time is the cost of outer loop, which is of O( n ),
# and thecost of list.insert( ... ), which is also of O( n ).
#
# It takes O( n^2 ) in total.

## Space Complexity: O( n )
#
# The overhead in space is the storage for list output, which is of O( n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'numbers indices')
def test_bench():

    test_data = [
                    TestEntry( numbers = [0,1,2,3,4], indices = [0,1,2,2,1] ),
                    TestEntry( numbers = [1,2,3,4,0], indices = [0,1,2,3,0] ),
                ]

    # expected output:
    '''
    [0, 4, 1, 3, 2]
    [0, 1, 2, 3, 4]
    '''

    for t in test_data:

        result = Solution().createTargetArray( nums = t.numbers, index = t.indices )
        
        print( result )

    return



if __name__ == '__main__' : 

    test_bench()