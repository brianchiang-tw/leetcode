'''

Description:

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]



Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''



from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:            

        def helper( left:int, right:int, string: List[str]):     
            
            if left >= right:
                # base case
                return
            
            # general case
            s[left], s[right] = s[right], s[left]
            
            helper( left+1, right-1, s)
        # ------------------------------------------------
        
        helper( left = 0, right = len(s)-1, string = s)



# n : the length of input char array, s


## Time Complexity: O( n )
#
# The overhead in time is the dpeth of recurion stack, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion stack, which is of O( n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'test_char_array' )

def test_bench():

    test_data = [
                    TestEntry( test_char_array = ["h","e","l","l","o"] ),
                    TestEntry( test_char_array = ["H","a","n","n","a","h"] ),
                ]

    # expected output:
    '''
    ['o', 'l', 'l', 'e', 'h']
    ['h', 'a', 'n', 'n', 'a', 'H']
    '''

    for t in test_data:

        Solution().reverseString( t.test_char_array )
        print(t.test_char_array)

    return



if __name__ == '__main__':

    test_bench()