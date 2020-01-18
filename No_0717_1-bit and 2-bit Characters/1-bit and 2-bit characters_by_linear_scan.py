'''

Description:

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.



Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.

'''



from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        index = 0
        
        size = len( bits )
        
        while index < size:
            
            if index == size-1 and bits[index] == 0:
                # last position ending with codeword 0
                return True
            
            if bits[index] == 1:
                # codeword 11, 10 move two steps forward
                index += 2
            else:
                # codeword 0, move one step forward
                index += 1
                
                
        return False



# n : the length of input list, bits.

## Time Complexity: O( n )
#
# The overhead in time is the while loop iterating on index, which is of O( n ).



## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping variable, which is of O( 1 ).


    
def test_bench():

    test_data = [
                    [1, 0, 0],
                    [1, 1, 1, 0]
                ]

    # expected output:
    '''
    True
    False
    '''

    for sequence in test_data:

        print( Solution().isOneBitCharacter(sequence) )
    
    return 



if __name__ == '__main__':
    
    test_bench()