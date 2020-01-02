'''

Description:

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

'''

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        left, right = 0, len(numbers)-1
        
        while left < right:
            
            summation = numbers[left] + numbers[right]
            
            if summation == target:
                return [left+1, right+1]
            
            elif summation > target:
                # summation is too big, make it smaller
                right -= 1
                
            else:
                # summation is too small, make it larger
                left += 1



# n : the length of input numbers:

## Time Complexity: O( n )
#
# The major overhead in time is the for while iterating on (left, right), which is of O( n )

## Space Complexity: O( n1 )
#
# The major overhead in space is the storage for pivot, left and right, which is of O( 1 )



def test_bench():

    test_data = [ 
                    ([2,7,11,15], 9),
                    ([2,7,11,15], 18)
                ]


    # expected output:
    '''
    [1, 2]
    [2, 3]
    '''

    for test_pair in test_data:

        print( Solution().twoSum(*test_pair) )

    return 



if __name__ == '__main__':

    test_bench()