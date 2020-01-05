'''

Description:

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

'''



class Solution:
    
    
    def check_substr(self, s, left, right):
    
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True
    
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        
        while left <= right:
            
            if s[left] == s[right]:
                
                left += 1
                right -= 1
            
            else:
                skip_one_on_right = s[left:right]
                
                if skip_one_on_right == skip_one_on_right[::-1]:
                    return True
                
                skip_one_on_left = s[left+1:right+1]
                
                if skip_one_on_left == skip_one_on_left[::-1]:
                    return True
                else:
                    return False
            
        return True


# n : the length of input string s

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on (left, right), which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for string slice, s[ l:r ], which is of O( n )




def test_bench():

    test_data = [
                    "aba",
                    "abca",
                    "abccad",
                    "abc",
                    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
                ]

    # expected output:
    '''
    True
    True
    False
    False
    True
    '''

    for s in test_data:

        print( Solution().validPalindrome(s) )

    return 



if __name__ == '__main__':

    test_bench()