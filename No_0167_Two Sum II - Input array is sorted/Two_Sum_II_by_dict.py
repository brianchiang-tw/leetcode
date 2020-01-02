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
        
        index_val_dict = dict()
        
        for i,x in enumerate(numbers):
            
            dual = target-x
            
            dual_exist = index_val_dict.get( dual, None)
            
            if dual_exist is not None:
                
                return [dual_exist+1, i+1]

            else:
                
                index_val_dict[x] = i
                


# n : the length of input numbers:

## Time Complexity: O( n )
#
# The major overhead in time is the for loop iterating on (i, x), which is of O( n )

## Space Complexity: O( n )
#
# The major overhead in space is the storage for dictionary, index_val_dict, which is of O( n )



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