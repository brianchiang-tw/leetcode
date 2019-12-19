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


class Solution:
    def defangIPaddr(self, address: str) -> str:

        output_str = address.replace( '.', '[.]' )

        return output_str




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