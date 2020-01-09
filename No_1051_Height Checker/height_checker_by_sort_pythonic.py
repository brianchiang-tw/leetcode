'''

Description:

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

 

Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.
 

Note:

1 <= heights.length <= 100
1 <= heights[i] <= 100

'''


from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        well_order = sorted( heights )
        
        counter_out_of_order = sum( x != y for x, y in zip(heights, well_order) )
                
        return counter_out_of_order



## Time Complexity: O( n log n ) on average case, O( n ^ 2) on worst case
#
# The overhead in time is the cost of sorting, which is O( n log n ) on average case, O( n ^ 2) on worst case

## Space Complexity: O( n )
#
# The overhead in space is the storage for list, well_order, which is of O( n )



def test_bench():

    test_data = [ 
                    [1,1,4,2,1,3],
                    [5,2,1,7,9,6]
                ]

    # expected output:
    '''
    3
    5
    '''

    for sequence in test_data:

        print( Solution().heightChecker(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()
