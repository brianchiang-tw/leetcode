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

class Solution:
    

    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        
        while left < right:
            
            # skip non-alphanumeric characters on left hand side
            while not s[left].isalnum() and left < right:
                left += 1
            
            # skip non-alphanumeric characters on right hand side
            while not s[right].isalnum() and left <right:
                right -=1
            
            # compare
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        
        return True



# n : the length of inputs string s

## Time Complexity: O( n )
#
# The major overhead in time is the while loop iterating on (left < right), which is of O( n ).


## Space Complexity: O( 1 )
#
# The compare is in-place, no need of extra space to copy string
# The major overhead in space is two-pointers (i.e., left and right), which is of O( 1 ).



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