'''

Description:

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

'''


class Solution:
    def convertToTitle(self, n: int) -> str:
        
        if n <=26:
            # base case
            return chr(64+n)
        
        else:
            if n % 26 == 0:
                # corner case handle for multiple of 26
                return self.convertToTitle( (n-1)//26 ) + self.convertToTitle( 26 )
            
            else:
                # general case
                return self.convertToTitle( (n-1)//26 ) + self.convertToTitle( (n) % 26 )



# n : the number of input

## Time Complexity: O( log n )
#
# The core procedure is a variant of base conversion from decimal to base 26.
# Thus, the depth of recursive call is of O( log n )

## Space Complexity: O( log n)
# The major overhead in space is to maintain call stack for recursive call, which is of O( log n )



def test_bench():

    test_data = [1, 25, 26, 27, 52, 53, 701]


    # expected output:
    '''
    A
    Y
    Z
    AA
    AZ
    BA
    ZY
    '''

    for n in test_data:

        print( Solution().convertToTitle(n) )

    return



if __name__ == '__main__':

    test_bench()