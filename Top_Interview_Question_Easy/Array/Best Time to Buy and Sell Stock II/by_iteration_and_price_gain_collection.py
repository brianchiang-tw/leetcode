'''

Description:

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.



Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.


             
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

'''


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        price_gain = 0
        
        for idx in range( len(prices)-1 ):
            
            if prices[idx] < prices[idx+1]:
                price_gain += ( prices[idx+1] - prices[idx] )
                
        return price_gain



# n : the length of input list, prices.

## Time Complexity: O( n )
#
# The overhead in time is the cost of for loop, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loopin index and temporary variable for profit, which is of O( 1 )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'stock_sequence')
def test_bench():

    test_data = [
                    TestEntry( stock_sequence = [7,1,5,3,6,4] ),
                    TestEntry( stock_sequence = [1,2,3,4,5] ),
                    TestEntry( stock_sequence = [7,6,4,3,1] ),
                ]

    # expected output:
    '''
    7
    4
    0
    '''

    for t in test_data:
        print( Solution().maxProfit( prices = t.stock_sequence) )

    return



if __name__ == '__main__':

    test_bench()
    