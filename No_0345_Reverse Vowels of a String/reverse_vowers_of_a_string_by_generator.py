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
        new_s = ''
        
        def rev_vowel( s:str):
            # Support function to collect vowel in reverse direction
            for char in reversed(s):
                if char in vowel:
                    yield char
        
        vowel_gen = rev_vowel(s)
        # Reverse vowels
        for char in s:
            
            if char in vowel:
                new_s += next( vowel_gen )
            else:
                new_s += char
                
        return new_s
                


# n : the length of input string, s.

## Time Complexity: O( n )
#
# The overhead in time is the for loop, iterating on s, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for new_s, which is of O( n ).



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