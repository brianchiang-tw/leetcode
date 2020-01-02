'''

Description:

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

'''


class Solution:
    
    
    def check_type_int(self, s: str) -> bool:
        try:
            
            int( float(s) )
            return True
        
        except ValueError:
            return False
            
    
    def myAtoi(self, str: str) -> int:
        
        # conrner case handling:
        # str is empty string
        if str == "":
            return 0

        
        tokens = str.split()

        # conrner case handling:
        # no valid token after parsing
        if len( tokens ) == 0:
            return 0
        
        integer = int(0)
        
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        
        sign = {'+','-'}
        with_sign = False
        last_position = 0

        for i in range( len(tokens[0]) ):
            
            char = tokens[0][i] 

            # check for '+' and '-'
            if i == 0 and char in sign :
                with_sign = True
            
            last_position += 1

            if i == 0 and with_sign:
                continue
            else:
                if char.isdecimal() is not True:

                    # skip the last character (not match to 0~9)
                    last_position -= 1
                    break

                

        str_slice = tokens[0][0:last_position]

      
        if self.check_type_int( str_slice ) is True:
            
            # convert to int, in range[ INT_MIN, INT_MAX ]
            integer = max( min( int( float(str_slice) ), INT_MAX), INT_MIN )
        else:
            pass

        
        return integer

# N : length of the input string

## Time Complexity: O( N )
#
# Preprocessing to exclude whitespace and to generate valid symbol takes O( N )
# Next, the workhorse is the for loop to scan each character also takes O( N )

## Space Complexity: O( 1 )
#
# Only need some variable for loop index, character/string operation and store the integer for ouput.


def test_bench():

    test_data = [ "", " ", "+1", "-1", "3.14159", "0", "Hello 1", "1 Hello", "  -0012a42", "   -42"]

    # expected output:
    '''

    0
    0
    1
    -1
    3
    0
    0
    1
    -12
    -42

    '''


    for x in test_data:

        atoi_value = Solution().myAtoi( x )

        print( "{}".format( atoi_value) )

    return


if __name__ == '__main__':

    test_bench()