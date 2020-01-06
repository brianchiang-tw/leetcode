'''

Description:

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
 

Constraints:

1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.

'''



import re
class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        # find all codes by regular expression
        regex = r'(\d\d#|\d)'
        pattern = re.compile(regex)

        codes = pattern.findall(s)

        # decoding by alphabet index 1~26 and ascii code
        plain_word = [ chr(int(code_str[:2])+96) for code_str in codes]
        
        plain_text = ''.join(plain_word)

        
        return plain_text



# n : the length of input string s

## Time Complexity: O( n )
#
# The major overhead in time is the pattern.findall and list comprehension for plain_word, 
# which are both of O( n ).


## Space Complexity: O( n )
#
# The major overhead in space is the storage for plain_word, and plain_text.
# They both take O( n ).


def test_bench():

    test_data = [
                    "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#",
                    "12310#11#12#321",
                    "10#11#12",
                    "1326#",
                    "25#",
                    "8512#12#15#23#15#18#12#4"
                ]

    # expected output:
    '''
    abcdefghijklmnopqrstuvwxyz
    abcjklcba
    jkab
    acz
    y
    helloworld
    '''


    for cipher_text in test_data:

        print( Solution().freqAlphabets(cipher_text) )

    return 



if __name__ == '__main__':

    test_bench()