'''

Description:

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".



Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3



Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
   Hide Hint #1  
For each stone, check if it is a jewel.

'''



from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewel = set(J)
        
        char_occ_dict = Counter(S)
        
        return sum( char_occ_dict[stone] for stone in char_occ_dict if stone in jewel )



# m : the length of J
# n : the length of S

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of set building of jewels, which is of O( m ),
# and the cost of counter building of stones, which is of O( n ).

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for set of jewels as well as counter of stones, which are of O( m + n ).

def test_bench():

    test_data = [
                    ("aA", "aAAbbbb"),
                    ("z", "ZZ")
                ]

    # expected output:
    '''
    3
    0
    '''

    for test_pair in test_data :

        print( Solution().numJewelsInStones( *test_pair ) )

    return 



if __name__ == '__main__':

    test_bench()