'''

Description:

Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

 

Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".



Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false 
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.



Example 3:

Input: s1 = "leetcodee", s2 = "interview"
Output: true
 

Constraints:

s1.length == n
s2.length == n
1 <= n <= 10^5
All strings consist of lowercase English letters.

'''



from string import ascii_lowercase
from collections import Counter    
    
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

 
        def break_another( dict_s1, dict_s2 ):
            
            s1_score, s2_score = 0, 0
            
            s1_win, s2_win = True, True
            
            for letter in reversed(ascii_lowercase):
                
                # scan from 'z' to 'a', (from strong letter to weak letter)
                
                s1_score += dict_s1[letter]
                s2_score += dict_s2[letter]
                
                # s1 break s2 if s1's score is larger than or equal to s2's score always, and vice versa.
                s1_win &= ( s1_score >= s2_score )
                s2_win &= ( s2_score >= s1_score )
            
            
            return s1_win or s2_win
            
        # --------------------------------------------
        
        ## dictionary
        # key: lowercase alphabet letter
        # value: occurrence
        dict_s1, dict_s2  = map( Counter, [s1, s2] )
        
        return break_another(dict_s1, dict_s2)



# n : the character length of string

## Time Complexity: O( n )
#
# The overhead in time is the cost of dictionary building, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in spaceis the storage for dictionary, which is of O( n )

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 's1 s2')

def test_bench():

    test_data = [
                    TestEntry(s1 = "abc", s2 = "xya" ),
                    TestEntry(s1 = "abe", s2 = "acd" ),
                    TestEntry(s1 = "leetcodee", s2 = "interview" ),
                ]

    for t in test_data:

        print( Solution().checkIfCanBreak( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()    