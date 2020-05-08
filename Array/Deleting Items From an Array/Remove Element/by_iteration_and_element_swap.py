'''

Description:

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}



Hint #1  

The problem statement clearly asks us to modify the array in-place and it also says that the element beyond the new length of the array can be anything. Given an element, we need to remove all the occurrences of it from the array. We don't technically need to remove that element per-say, right?



Hint #2  

We can move all the occurrences of this element to the end of the array. Use two pointers!



Hint #3  

Yet another direction of thought is to consider the elements to be removed as non-existent. In a single pass, if we keep copying the visible elements in-place, that should also solve this problem for us.

'''



from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        size = len( nums )
        
        prev, cur_idx = None, 0
        target_count = 0
        
        while cur_idx < size:
            
            if cur_idx == 0:
                # special handle for index 0                
                if nums[cur_idx] == val:
                    target_count += 1
               
            else:
                # general case
                
                if nums[cur_idx] == val:    
                    # update counter for val
                    target_count += 1
                
                elif prev == val:
                    # swap element
                    nums[ cur_idx ], nums[ cur_idx - target_count ] = nums[ cur_idx - target_count ], nums[ cur_idx ]
            
            # update previous element
            prev = nums[ cur_idx ]
            
            # update index for linear scan
            cur_idx += 1
            
        return size-target_count



# n : the length of input array, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary counter, which are of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence target')

def test_bench():

    test_data = [
                    TestEntry( sequence = [3,2,2,3], target = 3 ),
                    TestEntry( sequence = [0,1,2,2,3,0,4,2], target = 2 ),
                ]                        

    for t in test_data:

        print( Solution().removeElement( nums = t.sequence, val = t.target) )

    return



if __name__ == '__main__':

    test_bench()