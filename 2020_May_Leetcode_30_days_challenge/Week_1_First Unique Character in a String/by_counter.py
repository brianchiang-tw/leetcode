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
        
        for idx, char in enumerate(s):
            if char_occ_dict[char] == 1:
                return idx
        
        return -1



# n : the character length of input string

## Time Complexity: O( n )
#
# The overhead in time is the cost of dictionay building as well as for loop linear scan, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')



def test_bench():

    test_data = [
                    TestEntry( string = 'leetcode'),
                    TestEntry( string = 'loveleetcode'),
                    TestEntry( string = 'interview'),
                    TestEntry( string = 'onlinejudge'),
                    TestEntry( string = 'goodjob'),
                ]

    # expected output:
    '''
    0
    2
    1
    0
    0
    '''

    for t in test_data:
        print( Solution().firstUniqChar( s = t.string) )

    return



if __name__ == '__main__':

    test_bench()    