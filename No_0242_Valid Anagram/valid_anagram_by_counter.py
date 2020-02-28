'''

Desription:

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true



Example 2:

Input: s = "rat", t = "car"
Output: false



Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''



from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)


# n : the character length of input string

## Time Complexity: O( n )
#
# The overhead in time is the cost of dictionary building, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, Counter(s) as well as Counter(t), which is of O( n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 's t')
def test_bench():

    test_data = [
                    TestEntry( s= "anagram", t = "nagaram"),
                    TestEntry( s= "rat", t= "car"),
                ]

    # expected output:
    '''
    True
    False
    '''

    for t in test_data:

        print( Solution().isAnagram( s = t.s, t = t.t) )
    
    return 



if __name__ == '__main__':

    test_bench()
 