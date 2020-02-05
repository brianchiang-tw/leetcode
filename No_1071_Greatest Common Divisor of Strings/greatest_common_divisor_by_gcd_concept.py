'''

Description:

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.

'''



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if ( str1 + str2 ) != ( str2 + str1 ):
            return ''
        elif str1 == str2:
            return str1
        elif len(str1) > len(str2):
            return self.gcdOfStrings( str1[:len(str1)-len(str2)], str2 )
        else:
            return self.gcdOfStrings( str1, str2[:len(str2)-len(str1)] )



# n : the length of max( str1, str2)

## Time Complexity: O( log n )
#
# The overhead in time is the cost of gcd, which is of O( log n )


## Space Compleixty: O( n )
#
# The overhead in space is the storage for string concatenation, which is of O( n )



def test_bench():

    test_data = [
                    ("ABCABC", "ABC"),
                    ("ABABAB", "ABAB"),
                    ("LEET", "CODE")
                ]

    # expected output:
    # note: the third output is empty stirng ''
    '''
    ABC
    AB

    '''

    for string_1, string_2 in test_data:

        print( Solution().gcdOfStrings(string_1, string_2) )
    
    return 



if __name__ == '__main__':

    test_bench()