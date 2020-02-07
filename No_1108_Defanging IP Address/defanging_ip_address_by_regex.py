'''

Description:

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.

'''


from re import sub as re_sub
class Solution:
    def defangIPaddr(self, address: str) -> str:

        # \ is the escape character for dot symbol
        output_str = re_sub( '\.', '[.]', address )

        return output_str



# N : the lnegth of input string

## Time Complexity: O(1)
#
# The overhead in time is to repalce '.' by '[.]'.
# In addition, description grarantees that input string is valid IPv4 Address
# So there are at most 3 replacement to execute.

## Space Complexity: O(1)
#
# The overhead in space is to store the output string
# In addition, description grarantees that input string is valid IPv4 Address
# The worst cast is 255.255.255.255 -> 255[.]255[.]255[.]255 still of constant size.





def test_bench():

    test_data = [ "1.1.1.1", "255.100.50.0" ]

    # expected output:
    '''
    1[.]1[.]1[.]1
    255[.]100[.]50[.]0
    '''

    for test_str in test_data:

        print( Solution().defangIPaddr(test_str) )

    return



if __name__ == '__main__':

    test_bench()