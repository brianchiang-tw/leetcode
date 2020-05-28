'''

Description:

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]



Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

'''



from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        
        # Base case:
        # 0 = 0b 0 <-> ones count = 0
        ones_count = [0]
        
        for integer in range(1, num+1):
            
            # compute the quotient and remainder of interger / 2
            quotient, remainder = integer >> 1, integer & 1
            
            if remainder == 0:
                # even number
                ones_count.append( ones_count[quotient] )
            else:
                # odd number
                ones_count.append( ones_count[quotient] + 1 )
        
        return ones_count



# n : the value of num

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output ones_count, which is of O( n ).



def test_bench():

    test_data = [
                    1,  # [0, 1]
                    2,  # [0, 1, 1]
                    3,  # [0, 1, 1, 2]
                    4,  # [0, 1, 1, 2, 1]
                    5,  # [0, 1, 1, 2, 1, 2]
                    10, # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
                    20, # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2]
                    32, # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1]
                    64, # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 1]
                ]

    for n in test_data:

        print( Solution().countBits( n ) )

    return



if __name__ == '__main__':

    test_bench()