'''

Description:

Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
Example 4:

Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
Example 5:

Input: s = "friend", t = "family"
Output: 4
 

Constraints:

1 <= s.length <= 50000
s.length == t.length
s and t contain lower-case English letters only.

'''

from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s_occ_dict = defaultdict( int )
        t_occ_dict = defaultdict( int )
        
        # build the dictionary for input string s
        for ch in s:
            s_occ_dict[ch] += 1
        
        # build the dictionary for input string t
        for ch in t:
            t_occ_dict[ch] += 1
        
        
        # counting the minimum distance of anagram 
        diff = 0
        

        for ch in ascii_lowercase:
            
            diff += abs(s_occ_dict[ch] - t_occ_dict[ch])
            
        return diff//2



# n : the lenth of input word.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on ch, which are of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for dictionary, 
# s_occ_dict as well as t_occ_dict, which is of O( 1 )



def test_bench():

    test_data = [
                    ("bab", "aba"),
                    ("leetcode", "practice"),
                    ("anagram", "mangaar"),
                    ("xxyyzz", "xxyyzz"),
                    ("friend", "family")
                ]

    # expected output:
    '''
    1
    5
    0
    0
    4
    '''

    for string_s, string_t in test_data:

        print( Solution().minSteps(string_s, string_t) )
    
    return 



if __name__ == '__main__':

    test_bench()