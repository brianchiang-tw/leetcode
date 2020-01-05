'''

Description:

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # duplicate makes the length of set smaller than the one of original list
        return len(nums) != len( set(nums) )



def test_bench():

    test_data = [
                    [1,2,3,1],
                    [1,2,3,4],
                    [1,1,1,3,3,4,3,2,4,2]
                ]


    # expected output:
    '''
    True
    False
    True
    '''

    for test_arr in test_data:

        print( Solution().containsDuplicate(test_arr) )
    
    return 



if __name__ == '__main__':

    test_bench()