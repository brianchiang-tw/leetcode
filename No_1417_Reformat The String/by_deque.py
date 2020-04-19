'''

Description:

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.



Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.



Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.



Example 4:

Input: s = "covid2019"
Output: "c2o0v1i9d"



Example 5:

Input: s = "ab123"
Output: "1a2b3"
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.

'''



from collections import deque

class Solution:
    def reformat(self, s: str) -> str:
        
        # a deque to store letters
        letter = deque()
        
        # a deque to store numbers
        number = deque()
        
        for char in s:
            if char.isdigit():
                number.append( char )
            else:
                letter.append( char )
                
        if abs( len(letter)-len(number) ) >= 2:
            # Reject for no solution cases
            return ''
        
        
        # Judge which one has the longer sequence
        
        if len(letter) > len(number):
            longer, shorter = letter, number
        else:
            longer, shorter = number, letter
            
        output = []
        
        
        # Generate output string in interleaving between numbers and digits
        while shorter:
            output.append( longer.popleft() )
            output.append( shorter.popleft() )
        
        
        # Output the last element on tail
        if longer:
            output.append( longer.popleft() )
        
        
        return ''.join( output )



# n : the character length of input string

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan and linear output, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in storage is the cost of output, which is of the same length of input, in O( n ).

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')
def test_bench():

    test_data = [
                    TestEntry( string = "a0b1c2" ),
                    TestEntry( string = "leetcode" ),
                    TestEntry( string = "1229857369" ),
                    TestEntry( string = "covid2019" ),
                    TestEntry( string = "ab123" ),
                    TestEntry( string = "a" ),
                    TestEntry( string = "1" ),
                ]


    # expected output:
    '''
    0a1b2c


    c2o0v1i9d
    1a2b3
    a
    1
    '''

    for t in test_data:
        print( Solution().reformat( s = t.string) ) 

    return



if __name__ == '__main__':

    test_bench()