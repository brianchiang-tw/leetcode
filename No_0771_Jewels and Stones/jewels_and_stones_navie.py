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

'''


class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        count_of_stone_j = 0

        for j in J:
            count_of_stone_j += S.count(j)

        return count_of_stone_j


## Time Complexity: O( N )
#
# Since description guarantees J has no repetitions, thus checking s in j takes O(1)
# As a result, the overhead in time is the for loop of O( N )

## Space Complexity: O( 1 )
#
# The overhead in space is variable for math operation.

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