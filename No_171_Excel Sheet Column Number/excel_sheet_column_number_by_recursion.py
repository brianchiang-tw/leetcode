'''

Description:

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

'''



class Solution:
    def titleToNumber(self, s: str) -> int:
        
        if len(s) == 1:
            # base case
            return ord(s)-64

        else:
            # general case
            return 26*self.titleToNumber( s[:-1] ) + self.titleToNumber( s[-1] )



# n : the length of input string s

## Time Complexity: O( n )
#
# The major overhead in time is the call depth of recursion, which is of O( n ).

## Space Complexity: O( n )
#
# The major overhead in space is to maintain call stack for recursion, which is of O( n ).



def test_bench():

    test_data = ['A', 'AB', 'AZ', 'BA','ZY', 'ZZ','AAA']

    for s in test_data:

        n = Solution().titleToNumber(s)
        print(n)

    return



if __name__ == '__main__':

    test_bench()