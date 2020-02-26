'''

Description:

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2



Example 2:

Input: [3,1,3,4,2]
Output: 3



Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

'''



from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        slow, fast = 0, 0
        check = 0
        
        # let slow and fast meet in the loop of repeated numbers
        while True:
            
            slow = nums[ slow ]
            fast = nums[ nums[fast] ]
            
            if slow == fast:
                break
        
        # probing the repeated number
        while True:
            
            slow = nums[ slow ]
            check = nums[ check ]
            
            if slow == check:
                break
        
        return check



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [1,3,4,2,2] ),
                    TestEntry( sequence = [3,1,3,4,2] ),
                ]

    # expected output:
    '''
    2
    3
    '''

    for t in test_data:
        print( Solution().findDuplicate( nums = t.sequence ) )

    return 



if __name__ == '__main__':

    test_bench()