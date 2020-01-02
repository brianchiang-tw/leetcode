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

'''


class Solution:
    def removeDuplicates(self, nums ) -> int:
        
        if len(nums) == 0:
            return 0


        index_of_order = 0

        for j in range(1, len(nums)):

            if nums[j] != nums[ index_of_order ]:

                index_of_order += 1

                # move the next differnt increasing element to index_of_order
                nums[ index_of_order ] = nums[j]


        new_length = index_of_order + 1

        return new_length

# N: length of input list: nums

# Time complexity:
# Each iteration take O(1) comparison and assignment
# There are O(N) iterations in for loop


# Space complexity:
# O(1) for index_of_order to record the placeholder of next increasing element
# O(1) for j to visit each number in input list
# O(1) for computing the so-called "new length". (i.e., the number of different elements)




def test_bench():

    test_numbers = [0,0,1,1,1,2,2,3,3,4]

    length_of_modified_array = Solution().removeDuplicates( test_numbers )

    print( length_of_modified_array ) 
    # expected output
    '''
    5
    '''


if __name__ == "__main__":

    test_bench()