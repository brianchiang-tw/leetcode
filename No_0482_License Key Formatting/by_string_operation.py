'''

Description:

You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.



Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.

'''



class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        # Eliminate all dashes
        S = S.replace('-', '')
        
        head = len(S) % K
        
        grouping = []
        
        # Special handle for first group
        if head:
            grouping.append( S[:head] )
        
        # General case:
        for index in range(head, len(S), K ):
            grouping.append( S[ index : index+K ] )
        
        
        # Link each group togetger and separated by dash '-'
        return '-'.join( grouping ).upper()



# n : the character length of S

## Time Complexity: O( n ):
#
# The overhead in time is to make group, which is of O( n / 4) * 4 = O( n ).

## Space Complexity: O( n ):
#
# The overhead in space is the storage for outptu string, which is of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'license K')
def test_bench():

    test_data = [
                    TestEntry( license = "5F3Z-2e-9-w", K = 4),
                    TestEntry( license = "2-5g-3-J", K = 2),
                ]

    # expected output:
    '''
    5F3Z-2E9W
    2-5G-3J
    '''

    for t in test_data:

        print( Solution().licenseKeyFormatting( S = t.license, K = t.K) )

    return



if __name__ == '__main__':

    test_bench()