'''

Description:

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        
        # generate column-wise slicing
        column_slices, common_prefix = zip( *strs ), ''

        for current_column in column_slices:

            if len( set(current_column) ) == 1:

                # current column-wise slice's character is the same
                # update commin prefix

                common_prefix += current_column[0]
            
            else:
                
                # current column-wise slice's characters are different
                break
        
        return common_prefix


# N : total number of strings in input list
# S : the shortest length among all input strings, is constant

## Time complexity
# O( NS )       
# Each for loop take O(N) to make a set
# for loop iterates O(S) times totaly

# To sum up, time complexoty = O(  N * S ) = O( NS ) = O ( N )


## Space complexity
# O( S ) for saving the longest common prefix (at most equalt to shortest string on best chance)
# It is O( 1 ) in general


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().longestCommonPrefix( strs=["flower", "flow", "flight"] )
        self.assertEqual(result, 'fl')

    
    def test_case_2( self ):

        result = Solution().longestCommonPrefix( strs=["meow", "moo", "bark"] )
        self.assertEqual(result, '')


if __name__ == '__main__':

    unittest.main()

