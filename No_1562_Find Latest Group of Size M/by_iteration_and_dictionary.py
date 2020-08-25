'''

Description:

Given an array arr that represents a permutation of numbers from 1 to n. You have a binary string of size n that initially has all its bits set to zero.

At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1. You are given an integer m and you need to find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.

 

Example 1:

Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.



Example 2:

Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.



Example 3:

Input: arr = [1], m = 1
Output: 1



Example 4:

Input: arr = [2,1], m = 2
Output: 2
 

Constraints:

n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= n
All integers in arr are distinct.
1 <= m <= arr.length

'''


from typing import List
from collections import defaultdict

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        size = len(arr)
        
        if size == m:
            
            # Quick response for simple case
            # total m flips and m is equal to array size
            
            return size
        
        
        
        # key: length of substring with contiguous 1s
        # value: the count of substring with contiguous 1s with specified length, initialized as 0
        counter_of_len = defaultdict(lambda :0)
        
        
        # index: i
        # value: length of substring with contiguous 1s, which covers index i
        # +1 padding on head, +1 padding on tail, total + 2 to avoid index out-of-boundary
        len_of_cont_1s = [0] * ( size + 2 )
        
        
        last_good_step = -1
        
        # flip cur_idx to 1, and update information of length of 1s as well as count of 1s
        for step, cur_idx in enumerate(arr, 1):
            
            # get original length of 1s on left border and right border
            left_1s_length = len_of_cont_1s[cur_idx - 1]
            right_1s_length = len_of_cont_1s[cur_idx + 1]
            
            
            # compute the new length of 1s after flipping
            combined_1s_length = left_1s_length + 1 + right_1s_length
            
            
            # update new length of 1s on left borader and right border
            len_of_cont_1s[cur_idx - left_1s_length] = combined_1s_length
            len_of_cont_1s[cur_idx + right_1s_length] = combined_1s_length
            
            
            # update counter_of_len dictionary after flipping
            counter_of_len[combined_1s_length] += 1
            counter_of_len[left_1s_length] -= 1
            counter_of_len[right_1s_length] -= 1
                
                
            if counter_of_len[m] > 0:
                # now we still have substring of contiguous 1s with length exactly equal to m
                last_good_step = step
        
        
        return last_good_step


# n : the length of input list, arr

## Time Complexity: O( n )
#
# The overhead in time is the the cost of for loop iteration, and update on list as well as dictionary, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for list and dictionar, which are of O( n ).


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findLatestStep( arr = [3,5,1,2,4], m = 1 )
        self.assertEqual(result, 4)


    def test_case_2( self ):

        result = Solution().findLatestStep( arr = [3,1,5,4,2], m = 2 )
        self.assertEqual(result, -1)


    def test_case_3( self ):

        result = Solution().findLatestStep( arr = [1], m = 1 )
        self.assertEqual(result, 1)

    
    def test_case_4( self ):

        result = Solution().findLatestStep( arr = [2,1], m = 2 )
        self.assertEqual(result, 2)


if __name__ == '__main__':

    unittest.main()