'''

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2



Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # --------------------------------------------------------
        
        # helper function to generate next table for KMP algorithm
        def next_table(pattern):
            
            size_pattern = len(pattern)
            
            # optimal rollback table
            next_arr = [0 for _ in range(size_pattern)]
            
            next_arr[0] = -1
            
            i, j = 0, -1
            
            # compute next table with common prefix substring
            while i < size_pattern-1:
                
                if (j == -1) or (pattern[i] == pattern[j]):
                    
                    # first char, or common prefix exist
                    
                    i, j = i+1, j+1
                    next_arr[i] = j
                    
                else:
                    
                    # not match, roll back
                    j = next_arr[j]
            
            return next_arr
        
        # --------------------------------------------------------
        
        # Implement KMP algorithm
        
        if needle == '':
            
            # Return 0 for empty string as pattern
            return 0
        
        # compute optimal rollback table
        next_arr = next_table(needle)
        
        i, j = 0, 0
        size_src, size_pattern = len(haystack), len(needle)
        
        # keep compare character till the end of string
        while i < size_src and j < size_pattern:
            
            if (j == -1) or (haystack[i] == needle[j]):
                
                # if reset or character match, go to compare next one
                i, j = i+1, j+1
            
            else:
                # character mismatch, go back to optimal rollback index
                j = next_arr[j]
                
        
        if j == size_pattern:
            
            # Accept
            return i - size_pattern
        
        else:
            # Reject
            return -1


# m : length of haystack
# n : length of needle

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of KMP algorithm, which is of O( m + n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for next_arr table, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().strStr( haystack = "hello", needle = "ll" )
        self.assertEqual(result, 2)

    
    def test_case_2( self ):

        result = Solution().strStr( haystack = "aaaaa", needle = "bba" )
        self.assertEqual(result, -1)


    def test_case_3( self ):

        result = Solution().strStr( haystack = "", needle = "" )
        self.assertEqual(result, 0)


if __name__ == '__main__':

    unittest.main()