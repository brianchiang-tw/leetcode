'''

Description:

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]



Hint #1  

This is a really easy problem if you decide to use additional memory. For those trying to write an initial solution using additional memory, think counters!



Hint #2  

However, the trick really is to not use any additional space than what is already available to use. Sometimes, multiple passes over the input array help find the solution. However, there's an interesting piece of information in this problem that makes it easy to re-use the input array itself for the solution.



Hint #3  

The problem specifies that the numbers in the array will be in the range [1, n] where n is the number of elements in the array. Can we use this information and modify the array in-place somehow to find what we need?


'''


from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        

        for number in nums:

            present_indx = abs(number)-1
            if nums[present_indx] > 0 :
                # use negative number to mark number is presented in array
                nums[present_indx] = -nums[present_indx]
            else:
                pass


        # the disappeared numbers are those grids which are still with positive value
        return [ i+1 for i, num in enumerate(nums) if num > 0 ]



# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [4,3,2,7,8,2,3,1] ),
                    TestEntry( sequence = [3,2,2,3,1] ),
                    TestEntry( sequence = [3,4,3,5,3] ),
                ]

    # expected output:
    '''
    [5, 6]
    [4, 5]
    [1, 2]
    '''

    for t in test_data:

        print( Solution().findDisappearedNumbers( nums = t.sequence ) )
    
    return



if __name__ == '__main__':

    test_bench()