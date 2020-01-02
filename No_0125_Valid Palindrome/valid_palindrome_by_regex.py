'''

Description:

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''


import re

class Solution:
    
    def refine(self, s:str) ->str:
    
        regex = r'[^A-Za-z0-9]'
        pattern = re.compile(regex)
        
        return pattern.sub('', s)
    
    def isPalindrome(self, s: str) -> bool:
        
        alphanumeric_s = self.refine(s).lower()
        
        return alphanumeric_s == alphanumeric_s[::-1]



# n : the length of inputs string s

## Time Complexity: O( n )
#
# The major overhead in time is the refine function and [::-1] string copy, which is of O( n ).


## Space Complexity: O( n )
#
# The compare is out-of-place, need extra space of O( n )
# The major overhead in space is storage for out-of-place comparison, which is of O( n )



def test_bench():

    test_data = [
                    "A man, a plan, a canal: Panama",
                    "race a car"
                ]

    # expected output:
    '''
    True
    False
    '''

    for test_s in test_data:

        print( Solution().isPalindrome(test_s) )
    
    return 



if __name__ == '__main__':

    test_bench()