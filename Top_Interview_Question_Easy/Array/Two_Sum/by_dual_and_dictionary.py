'''

Description:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
   


   Hint #1  
A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions for just for completeness. It is from these brute force solutions that you can come up with optimizations.



   Hint #2  
So, if we fix one of the numbers, say
x
, we have to scan the entire array to find the next number
y
which is
value - x
where value is the input parameter. Can we change our array somehow so that this search becomes faster?



   Hint #3  
The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

'''



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_idx_dict = {}
        
        for idx, number in enumerate(nums):
            
            # compute dual
            dual = target-number
            
            if dual in num_idx_dict:
                # check if dual exist
                return [ num_idx_dict[dual], idx ]
            
            else:
                # update number-index dictionary
                num_idx_dict[ number ] = idx



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence target')

def test_bench():

    test_data = [
                    TestEntry( sequence = [2, 7, 11, 15], target = 9 ),
                    TestEntry( sequence = [2, 7, 11, 15], target = 13 ),
                    TestEntry( sequence = [2, 7, 11, 15], target = 17 ),
                    TestEntry( sequence = [2, 7, 11, 15], target = 18 ),
                    TestEntry( sequence = [2, 7, 11, 15], target = 26 ),
                ]


    # expected output:
    '''
    [0, 1]
    [0, 2]
    [0, 3]
    [1, 2]
    [2, 3]
    '''

    for t in test_data:

        print( Solution().twoSum( nums = t.sequence, target = t.target ) )

    return



if __name__ == '__main__':

    test_bench()                    