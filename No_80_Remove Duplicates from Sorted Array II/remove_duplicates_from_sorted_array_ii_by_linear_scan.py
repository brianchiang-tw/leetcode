'''

Desription:

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

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

'''



from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        last_head, length = 0, 0
        insert_pos = 0
        
        for i, cur in enumerate(nums):
            
            if i == 0:
                # Initial case:
                
                last_head = cur
                length = 1
                insert_pos += 1
                
            else:
                # General case:
                
                if cur == last_head:
                    
                    if length < 2:
                        
                        length += 1
                        nums[ insert_pos ] = cur
                        insert_pos += 1
                    
                    else:
                        
                        # remove duplicate element whose length is over 2
                        # keep idle until another different new element is met
                        length += 1
                        
                else:
                    
                    length = 1
                    
                    last_head = cur
                    nums[ insert_pos ] = cur
                    insert_pos += 1



        # new length of decorated array                    
        return insert_pos


# n : the length of input sorted array

## Time Complexity: O( n )
#
# The major overhead in time is the for loop iterting in (i, cur), which is of O( n ).

## Space Complexity: O( 1 )
#
# All the update and modficiation is in-place.
# Thus, the overhead in space is of O( 1 ).



def test_bench():

    test_data = [
                    [1,1,1,2,2,3],
                    [0,0,1,1,1,1,2,3,3],
                    [1],
                    []
                ]

    # expected output:
    '''
    k = 5, result = [1, 1, 2, 2, 3]
    k = 7, result = [0, 0, 1, 1, 2, 3, 3]
    k = 1, result = [1]
    k = 0, result = []
    '''

    for test_arr in test_data:

        k = Solution().removeDuplicates( test_arr )

        print( f'k = {k}, result = {test_arr[:k]}' )

    return 



if __name__ == '__main__':

    test_bench()