'''

Description:

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.



Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.



Example 3:

Input: s = "triplepillooooow"
Output: 5



Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11



Example 5:

Input: s = "tourist"
Output: 1
 

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.

'''



class Solution:
    def maxPower(self, s: str) -> int:
        
        # the minimum value for consecutive is 1
        local_max, global_max = 1, 1
        
        # dummy char for initialization
        prev = '#'
        for char in s:
            
            if char == prev:
                
                # keeps consecutive, update local max
                local_max += 1
                
                # update global max length with latest one
                global_max = max( global_max, local_max )
                
            else:
                
                # lastest consective chars stops, reset local max
                local_max = 1
            
                # update previous char as current char for next iteration
                prev = char
        
        
        return global_max



# n : the character length of input string, s 

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear iteration, which is of O( n ).

## Space Compleixty: O( 1 )
#
# The overhead in space is the storage for loop index and temporary vairalbe, which is of O( 1 ).



def test_bench():

    test_data = [
                    "leetcode",
                    "abbcccddddeeeeedcba",
                    "triplepillooooow",
                    "hooraaaaaaaaaaay",
                    "tourist",
                ]

    # expected output:
    '''
    2
    5
    5
    11
    1
    '''

    for test_string in test_data:

        print( Solution().maxPower(test_string) )

    return        



if __name__ == '__main__':

    test_bench()