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
        
        # corner case handling
        if len(strs) == 0:
            return ""
        
        # to memorize longest common prefix
        longest_common_prefix = str()
        
        
        # get the shortest string among those strings in input strs
        shortest_string = min( strs, key = len )
        
        # check if other string has common prefix with shortest string
        for i in range( len(shortest_string) ):
            
            if all( string[i]==shortest_string[i] for string in strs ):
                # match one common character
                # update longest common prefix
                longest_common_prefix += shortest_string[i]
                
            else:
                # no match anymore
                # leave for loop
                break
                
        
        return longest_common_prefix

# N : total number of strings in input list
# S : the shortest length among all input strings, is constant

# Time complexity
# O( NS )       
# Each for loop take O(1) character comparison
# If statesments take O(N) iterations
# for loop iterates O(S) times totaly

# To sum up, time complexoty = O( 1 * N * S ) = O( NS ) = O ( N )


 # Space complexity
 # O( S ) for saving the longest common prefix (at most equalt to shortest string on best chance)
 # It is O( 1 ) in general


def test_bench():

    test_strings_1 = ["flower", "flow", "flight"]
    test_strings_2 = ["meow", "moo", "bark"]

    output_1 = Solution().longestCommonPrefix( test_strings_1 )
    print( output_1 )

    output_2 = Solution().longestCommonPrefix( test_strings_2 )
    print( output_2 )

    # expected output
    # Note: 
    # the second output is "", empty string, 
    # because "meow", "moo", and "bark" have no common sequence at all.
    '''
    fl

    '''


if __name__ == "__main__":

    test_bench()