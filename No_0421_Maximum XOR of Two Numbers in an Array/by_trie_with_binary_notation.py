'''

Description:

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

'''


class Solution(object):
    def findMaximumXOR(self, nums):
        
        trie = {}
        
        # ------------------------------
        
        def update_trie(x):
            # update trie with binary representation of x
            
            cur = trie
            for bit in format(x, '032b'):
                
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]
                
            cur['value'] = x
            
            return
        
        # ------------------------------
             
        def best_match(x):
            # try to match with complement of x as much as possible
            
            # recall that for xor opertator
            # 1 xor 0 = 1
            # 0 xor 1 = 1
            # 0 xor 0 = 1 xor 1 = 0
            
            cur = trie
            for bit in format(x, '032b'):
                
                rev = '0' if bit == '1' else '1'
                
                if rev in cur:
                    cur = cur[rev]
                else:
                    cur = cur[bit]
                    
            return cur['value']
        
        # ------------------------------
        
        for x in nums:
            update_trie(x)
        
        max_xor = 0
        for x in nums:
            
            # update global maximal xor result
            max_xor = max( max_xor, x ^ best_match(x) )
         
        return max_xor


# n :　the length of nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( 32n ) = O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for the trie, which is of O( 32n ) = O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findMaximumXOR( nums=[3, 10, 5, 25, 2, 8] )
        self.assertEqual(result, 28 )


if __name__ == '__main__':
    unittest.main()