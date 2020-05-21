'''

Description:

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

'''


from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        # a stack with monotonic decreasing
        monotonic_stack = []
        
        # dictionary:
        # key: number
        # value: next greater number of key
        dict_of_greater_number = {}

        # ----------------------------------------------
        
        # launch linear scan to build dict_of_greater_number
        for cur_number in nums2:
            
            # maintain a monotonic decreasing stack
            while monotonic_stack and cur_number > monotonic_stack[-1]:
                
                pop_out_number = monotonic_stack.pop()
                
                # next greater number of pop_out_number is cur_number
                dict_of_greater_number[pop_out_number] = cur_number
            
            monotonic_stack.append(cur_number)
        # ----------------------------------------------
        
        # solution output
        next_greater_element = []
        
        # get next greater element by dictionary
        for x in nums1:
            
            if x in dict_of_greater_number:
                next_greater_element.append( dict_of_greater_number[x] )
                
            else:
                next_greater_element.append(-1)
                
        return next_greater_element


# n : number of elements in input nums2

## Time Complexity: O( n )
#
# The overhead in time is the linear scan and operation of monotonic stack, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is to maintain a dictionary and output list
# Both of them take O( n )


def test_bench():

    test_data = [ 
                    ( [4,1,2], [1,3,4,2] ),
                    ( [2,4], [1,2,3,4] )
                ]


    # expected output:
    '''
    [-1, 3, -1]
    [3, -1]
    '''


    for test_pair in test_data:

        next_greater_element = Solution().nextGreaterElement( *test_pair)

        print( next_greater_element )

    return



if __name__ == '__main__':

    test_bench()