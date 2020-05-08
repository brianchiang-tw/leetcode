'''

Description:

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}



Hint #1  

In this problem, the key point to focus on is the input array being sorted. As far as duplicate elements are concerned, what is their positioning in the array when the given array is sorted? Look at the image above for the answer. If we know the position of one of the elements, do we also know the positioning of all the duplicate elements?



Hint #2  

We need to modify the array in-place and the size of the final array would potentially be smaller than the size of the input array. So, we ought to use a two-pointer approach here. One, that would keep track of the current element in the original array and another one for just the unique elements.



Hint #3  

Essentially, once an element is encountered, you simply need to bypass its duplicates and move on to the next unique element.

'''



from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev, size = None, len(nums)
        unique_pos, current_pos = 0, 0
        
        while current_pos < size:
            
            if nums[current_pos] != prev:
                # catch and move unique element
                nums[unique_pos] = nums[current_pos]
                
                # update index enxt next unique element
                unique_pos += 1
            
            # update previous element for next iteration
            prev = nums[current_pos]    
            
            # update index for linear element scan
            current_pos += 1
        
        return unique_pos



# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for two-pointer and loop index, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [1,1,2] ),
                    TestEntry( sequence = [0,0,1,1,1,2,2,3,3,4] ),
                ]        

    # expected output:
    '''
    2
    5
    '''

    for t in test_data:

        print( Solution().removeDuplicates( nums = t.sequence ) )

    return



if __name__ == '__main__':

    test_bench()