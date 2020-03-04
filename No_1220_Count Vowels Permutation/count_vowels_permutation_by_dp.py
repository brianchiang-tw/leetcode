'''

Description:

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".



Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".



Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4

'''




class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        modulo = 10**9 + 7
        
        # initialization for length of permutation = 1
        (a, e, i, o, u) = (1, 1, 1, 1, 1)
        
        length_of_permutation = 2
        while length_of_permutation <= n:
            
            # update total method count by transition rule
            end_with_a = e + i + u
    
            end_with_e = a + i

            end_with_i = e + o
           
            end_with_o = i
   
            end_with_u = i + o
            
            # update method count of ending with a e i o u
            (a, e, i, o, u) = (end_with_a, end_with_e, end_with_i, end_with_o, end_with_u )
            
        
            length_of_permutation += 1
        

        return (a + e + i + o + u) % modulo



# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the while loop, iterating on n, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index, and dynamic programming vvariable, which is of O( 1 ).

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string_length')

def test_bench():

    test_data = [
                    TestEntry( string_length = 1),
                    TestEntry( string_length = 2),
                    TestEntry( string_length = 3),
                    TestEntry( string_length = 4),
                    TestEntry( string_length = 5),
                    TestEntry( string_length = 10),
                    TestEntry( string_length = 2*10**4),
                ]

    # expected output:
    '''
    5
    10
    19
    35
    68
    1739
    759959057
    '''

    for t in test_data:
        print( Solution().countVowelPermutation( n = t.string_length) )

    return



if __name__ == '__main__':

    test_bench()