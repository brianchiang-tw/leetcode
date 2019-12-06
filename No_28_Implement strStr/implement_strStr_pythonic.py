class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # corner case handling for needle is empty string
        if needle is "":
            return 0
        
        
        m, n = len(haystack), len(needle)
        for i in range( m - n + 1 ):
            
            if haystack[ i : (i+n) ] == needle:
                return i

        # if no match, return -1    
        return -1



# M : length of haystack
# N : length of needle

## Time Complexity: O( M*N )
#
# The overhead is the nested loops, outer for loop takes O( M ), while inner one takes O( N )

## Space Complexity: O( 1 )
#
# The overhead is some variables for index of looping and substring.


def test_bench():

    test_data = [
                    ("hello", "ll"),
                    ("hello", "ho"),
                    ("hello", ""),
                    ("hello", "hello")
                ]

    # expected output
    '''
    2
    -1  
    0
    0
    '''


    for test_pair in test_data:

        index_of_match = Solution().strStr( *test_pair )

        print( index_of_match )

    
    return


if __name__ == '__main__':

    test_bench()