class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        vowel = set("aeiouAEIOU")
        
        return ' '.join([ t +'ma'+'a'*idx if t[0] in vowel else t[1:] + t[0] + 'ma'+'a'*idx for idx, t in enumerate( S.split(), 1 ) ])



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