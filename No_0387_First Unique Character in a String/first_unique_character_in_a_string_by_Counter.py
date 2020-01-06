'''

Description:

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''



from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        char_occ_dict = Counter(s)
        
        
        unique_char = [ c for c, occ in char_occ_dict.items() if occ == 1]
        
        if len(unique_char) == 0:
            return -1
        else:
            return s.index( unique_char[0] )


# n : the length of input string, s.

## Time Complexity: O( n )
#
# The overhead in time is the ditionary building of char_occ_dict, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for dicionary, which is of O( n ).



def test_bench():

    test_data = [
                    "leetcode",
                    "loveleetcode",
                    "helloworld",
                    "aabbccddee"
                ]

    # expected output:
    '''
    0
    2
    0
    -1
    '''


    for test_s in test_data:
        print( Solution().firstUniqChar(test_s) )

    return 



if __name__ == '__main__':

    test_bench()