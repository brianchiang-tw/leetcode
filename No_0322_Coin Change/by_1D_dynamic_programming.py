'''

Description:

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1



Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

'''



from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp_table = [ float('inf') for _ in range(amount+1) ]
        
        # base case for $0
        dp_table[0] = 0
        
        for value in range(1, amount+1):
            for coin in coins:
                if coin > value:
                    continue
                
                # update dp_table, try to make change with coin
                dp_table[value] = min( (dp_table[value], dp_table[ value - coin ] + 1) )
        
        if dp_table[amount] != float('inf'):
            # Accept, return total count of coin change
            return dp_table[amount]
        else:
            # Reject, no solution
            return -1



# c : the length of coins array
# n : the value of amount

## Time Complexity: O( c * n )
#
# The overhead in time is the nested loops, which is of O( c * n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dynamic programming table, which is of O( n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'coins amount')

def test_bench():

    test_data = [
                    TestEntry( coins = [1, 2, 5], amount = 11),
                    TestEntry( coins = [2], amount = 3),
                    TestEntry( coins = [2], amount = 4),
                    TestEntry( coins = [2], amount = 0),
                ]

    # expected output:
    '''
    3
    -1
    2
    0
    '''

    for t in test_data:

        print( Solution().coinChange( *t ) )

    return



if __name__ == '__main__':

    test_bench()