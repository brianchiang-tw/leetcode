'''

Description:

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''

# Note: Description demands us to implement in O(1) space

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        half_way = len(s)//2
        for i in range( half_way ):
            
            s[i], s[-(i+1)] = s[-(i+1)], s[i] 
            
        return



# n : the length of input list

## Time Compleixty: O( n )
#
# The overhead in time is the length of halfway of O( n ), which controls the iterations of for loop

## Space Complexity: O( 1 )
#
# Each re-arrangement takes O( 1 ) as temp buffer for element swap.



def test_bench():

    test_data = [
                    ["h","e","l","l","o"],
                    ["H","a","n","n","a","h"]
                ]


    # expected output:
    '''
    ['o', 'l', 'l', 'e', 'h']
    ['h', 'a', 'n', 'n', 'a', 'H']
    '''

    for test_list in test_data:

        Solution().reverseString( test_list )
        print( test_list )

    return 



if __name__ == '__main__':

    test_bench()