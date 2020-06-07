'''

Description:

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1



Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.



Example 3:

Input: amount = 10, coins = [10] 
Output: 1
 

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer

'''



from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # base case:
        # amount 0's method count = 1 (by taking no coins)
        change_method_count = [1] + [ 0 for _ in range(amount)]
        
        # make change with current coin
        for cur_coin in coins:
            
            # update change method count from small amount to target amount
            for small_amount in range(cur_coin, amount+1):
                
                # current small amount can make changed with current coin
                change_method_count[small_amount] += change_method_count[small_amount-cur_coin]
            
        return change_method_count[amount]



# m : the value of amount
# n : the length of coins array

## Time Complexity: O( m*n )
#
# The overhead in time is the cost of nested loops, which is of of O( m * n )

## Space Complexity: O( m )
#
# The overhead in space is the storage for dynamic programming table, change_method_count, which is of O( m )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'amount coins')

def test_bench():

    test_data = [
                    TestEntry( amount = 5, coins = [1, 2, 5] ),
                    TestEntry( amount = 3, coins = [2] ),
                    TestEntry( amount = 10, coins = [10] ),
                    TestEntry( amount = 10, coins = [1,2,5,10] ),
                ]

    # expected output:
    '''
    4
    0
    1
    11
    '''


    for t in test_data:

        print( Solution().change( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()