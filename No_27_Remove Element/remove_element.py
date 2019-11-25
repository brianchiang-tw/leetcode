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

'''



class Solution:
    def removeElement(self, nums, val) -> int:
        
        # variable initialization
        index_of_rearrange = None
        length_of_valid_element = 0
        
        # visit each element in list: nums
        for i in range( len(nums) ):
            
            
            if index_of_rearrange == None and nums[i] == val:
                # first time, meet a element = value, assign index_of_rearrange
                index_of_rearrange = i
            
            
            elif index_of_rearrange == None and nums[i] != val:
                # meet valid element before invalid element's occurrence

                # update length of valid element
                length_of_valid_element += 1
                
            elif index_of_rearrange != None and nums[i] == val:
                # meet invalid element
                pass
            
            elif index_of_rearrange != None and nums[i] != val:
                # meet valid element after invalid element's occurrence

                # move valid element to index_of_rearrange
                nums[ index_of_rearrange ] = nums[i]

                # update index of rearrange
                index_of_rearrange += 1
                
                # add length of valid element by 1
                length_of_valid_element += 1
                
        return length_of_valid_element

# N = total count of elements in input list nums
#   = length of input list nums


# Time Complexity:
# Each iteration take O(1) for comparison, index and length_of_valid element update
# In summary, we have O(N) iterations in for loop

# Space Complexity:
# Only O(1) for index_of_rearrange as well as length_of_valid_element




def test_bench():

    test_numbers =  [   ([3,2,2,3], 3),
                        ([0, 1, 2, 2, 3, 0, 4, 2], 2)
                    ]

    # expected output
    '''
    2
    5
    '''

    for test_set in test_numbers:

        new_length = Solution().removeElement( nums = test_set[0], val = test_set[1] )

        print( new_length )

    return






if __name__ == "__main__":

    test_bench()