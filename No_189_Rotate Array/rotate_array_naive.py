'''

Description:

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

'''

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # naive implementation
        for _ in range(k):
            
            right_most = nums.pop()
            nums.insert(0, right_most )
            
        return


# N : the length of input array nums
# k : the times of rotation

## Time complexity: O( k )
#
# The overhead is the for loop on k of O( k )

## Space complexity: O( 1 )
#
# The overhead is the variable for loop index and temp buffer for right most element.



def test_bench():

    test_data = [ 
                    ([1, 3, 5, 7, 9], 2),
                    ([1, 3, 5, 7, 9], 11)
                ]

    # expected output:
    '''
    [7, 9, 1, 3, 5]
    [9, 1, 3, 5, 7]
    '''

    for test in test_data:

        Solution().rotate( test[0], test[1] )
        print( test[0] )

    
    return



if __name__ == '__main__':

    test_bench()