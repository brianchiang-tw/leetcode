'''

Description:

We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are a elements with value b in the decompressed list.

Return the decompressed list.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4,4] is [2,4,4,4].
 

Constraints:

2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100

'''



from typing import List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        decode_output= []
        
        for i in range( 0, len(nums), +2):
            
            frequency = nums[i]
            value     = nums[i+1]
            decode_output.extend( [value ] * frequency )
            
            
        return decode_output


# n : the length of input list, nums.
# k : the highest freqeuncy of run-length-encoding.


## Time Complexity: O( n * k )
#
# The overhead in time is the for loop iterating on i, and element duplicate of frequency.
# It takes O( n * k ) in total.



## Space Complexity: O( n * k )
#   
# The overhead in space is the storage for output, decode_output, which is of O( n * k )



def test_bench():

    test_data = [
                    [1,2,3,4],
                    [1,3,2,5],
                    [1,2,3,4,5,6]
                ]

    # expected output:
    '''
    [2, 4, 4, 4]
    [3, 5, 5]
    [2, 4, 4, 4, 6, 6, 6, 6, 6]
    '''


    for encoding_of_RLE in test_data:

        print( Solution().decompressRLElist(encoding_of_RLE) )

    return 



if __name__ == '__main__':

    test_bench()