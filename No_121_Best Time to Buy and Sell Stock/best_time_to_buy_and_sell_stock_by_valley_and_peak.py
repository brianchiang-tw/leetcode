'''

Description:

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

''' 


from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            # corner case
            return 0
        
        min_price, min_index = 2**31, 0
        max_price, max_index = 0, 0
        
        max_profit = 0
        
        for i, p in enumerate(prices):
            
            if p <= min_price:
                # update valley
                min_price = p
                min_index = i
            
            if p >= min_price:
                # update peak
                max_price = p
                max_index = i
                
            
            if max_index > min_index and (max_price - min_price) > max_profit :
                # update max_profit
                max_profit = max_price - min_price
                
                
        return max_profit
            


# n : the length of input array, prices.

## Time Complexity: O( n )
#
# The major overhead in time is the for loop iterating on (i, p), which is of O( n ).

## Space Complexity: O( 1 )
#
# The major overhead in space is the variables for price computation, which is of O( 1 ).



def test_bench():

    test_data = [
                    [7,1,5,3,6,4],
                    [7,6,4,3,1],
                    [2,4,1],
                    []
                ]

    # expected output:
    '''
    5
    0
    2
    0
    '''

    for stock_price in test_data:

        print( Solution().maxProfit(stock_price) )

    return



if __name__ == '__main__':

    test_bench()