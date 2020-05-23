'''

Description:

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.

 

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3

Explanation: 
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.



Example 2:

Input: heights = [5,1,2,3,4]
Output: 5



Example 3:

Input: heights = [1,2,3,4,5]
Output: 0
 

Constraints:

1 <= heights.length <= 100
1 <= heights[i] <= 100



Hint #1  

Build the correct order of heights by sorting another array, then compare the two arrays.

'''



from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        well_order = sorted( heights )
        
        out_of_order = 0
        for i in range( len(heights) ):
            
            if well_order[i] != heights[i]:
                out_of_order += 1
                
        return out_of_order



# n : the length of input list, heights

## Time Complexity : O( n log n )
#
# The overhead in time is the cost of sorting, which is O( n log n ) in Python.

## Space Complexity: O( n )
#
# The overhead in space is the storage for another list, well_order, which is of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [1,1,4,2,1,3] ),
                    TestEntry( sequence = [5,1,2,3,4] ),
                    TestEntry( sequence = [1,2,3,4,5] ),
                ]

    # expected output:
    '''
    3
    5
    0
    '''

    for t in test_data:

        print( Solution().heightChecker( heights= t.sequence ) )

    return



if __name__ == '__main__':

    test_bench()