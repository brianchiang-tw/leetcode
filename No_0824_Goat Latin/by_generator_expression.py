'''

Description:

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"



Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
 

Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.

'''


class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        vowel = set("aeiouAEIOU")
        
        return ' '.join( t +'ma'+'a'*idx if t[0] in vowel else t[1:] + t[0] + 'ma'+'a'*idx for idx, t in enumerate( S.split(), 1 ) )



# n : the character length of input S

## Time Complexity: O( n )
#
# The overhead in time is the cost of generator expression, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the cost of output string, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')
def test_bench():

    test_data = [
                    TestEntry( string = "I speak Goat Latin" ),
                    TestEntry( string = "The quick brown fox jumped over the lazy dog" ),
                ]

    # expected output:
    '''
    Imaa peaksmaaa oatGmaaaa atinLmaaaaa
    heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa
    '''

    for t in test_data:
        print( Solution().toGoatLatin( S = t.string) )

    return



if __name__ == '__main__':

    test_bench()