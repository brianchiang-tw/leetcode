'''

Description:

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

'''

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        
        stack_running = [ ]
        
        next_greater_element = [ -1 ] * size
        
        for i in range( size * 2):
            
            current = nums[ i % size ]
            
            while stack_running and nums[ stack_running[-1] ] < current:
                
                next_greater_element[ stack_running[-1] ] = current
                stack_running.pop()
                
            
            if i < size:
                stack_running.append( i )
        
        return next_greater_element



# N : number of element in input nums

## Time Complexity: O( N )
#
# The overhead in time is the outer for loop of O( N )
# the inner while loop on stack is amortized O( 1 )

## Space Complexity: O( N )
#
# The overhead in space is to maintain a stack and output list for next great element
# Both of them take O( N )



def test_bench():

    test_data = [ 101, 3, 5, 4, 2, 99, 50, 100]

    next_greater_element = Solution().nextGreaterElements( test_data )

    # expected output:
    '''
    [-1, 5, 99, 99, 99, 100, 100, 101]
    '''
    print( next_greater_element )

    return



if __name__ == '__main__':

    test_bench()