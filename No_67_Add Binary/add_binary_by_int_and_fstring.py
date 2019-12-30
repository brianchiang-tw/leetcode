'''

Description:

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        return f'{(int(a, 2) + int(b, 2)):b}'



def test_bench():

    test_data = [
                    ('11', '1'),
                    ('1010', '1011')
                ]
    
    # expected output:
    '''
    100
    10101
    '''
    

    for test_pair in test_data:
        print( Solution().addBinary( *test_pair ) )

    return 



if __name__ == '__main__':

    test_bench()

