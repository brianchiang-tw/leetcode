'''

Description:

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        xor_result = x ^ y
        hamming_dist = 0
        
        for bit_shift in range(32):
            
            if xor_result & 1:
                hamming_dist += 1
            
            xor_result >>= 1
        
        return hamming_dist



## Time Complexity: O( 1 )
#
# The overhead in time is the cost of xor and loop, which is of O(32) = O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):
        result = Solution().hammingDistance(1, 4)
        self.assertEqual(result, 2)
    

if __name__ == '__main__':

    unittest.main()    
