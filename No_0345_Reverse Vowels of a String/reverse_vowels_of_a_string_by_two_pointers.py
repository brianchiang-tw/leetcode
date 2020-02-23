'''

Description:

Write a function that takes a string as input and reverse only the vowels of a string.



Example 1:

Input: "hello"
Output: "holle"



Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

'''



class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowel = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}
        
        new_s = list(s)
        last_index = len(s)-1
        left, right = 0, last_index
        
        while left <= right:
            
            while left <= right and s[left] not in vowel: left +=1
            while left <= right and s[right] not in vowel: right -=1
            
            if left > right:
                break
            
            new_s[ left ], new_s[ right ] = new_s[ right ], new_s[ left ]
            
            left, right = left+1, right-1
            
        return ''.join(new_s)



# n : the length of input string, s.

## Time Complexity: O( n )
#
# The overhead in time is the for outer while loop,  which are of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for list, new_s, which is of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')

def test_bench():

    test_data = [
                    TestEntry('hello'),
                    TestEntry('leetcode'),
                    TestEntry('challenge'),
                ]

    for t in test_data:

        print( Solution().reverseVowels(t.string) )

    return 



if __name__ == '__main__':

    test_bench()