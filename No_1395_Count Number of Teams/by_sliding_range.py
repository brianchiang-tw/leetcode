'''

Description:

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 



Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.



Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5

'''



from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        r, size = rating, len( rating )
        
        left_smaller = [ sum( r[i] < r[j] for i in range(0,j) ) for j in range(size) ]
        right_bigger = [ sum( r[j] < r[k] for k in range(j+1, size) ) for j in range(size)]
        
        num_of_teams = 0
        for j in range( 0, size):
            num_of_ascending_team = left_smaller[j] * right_bigger[j]
            num_of_descending_team = ( j - left_smaller[j] ) * ( size-1 - j - right_bigger[j] )
            
            num_of_teams += ( num_of_ascending_team + num_of_descending_team )
            
        return num_of_teams



# n : the length of input list, rating.

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost of table computation, including left_smaller and right_bigger, which is of O( n ^ 2 )

## Space Complexity: O( n )
#
# The overhead in space is the storage for table, including left_smaller and right_bigger, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'rating')

def test_bench():

    test_data = [
                    TestEntry( rating = [2,5,3,4,1] ),
                    TestEntry( rating = [2,1,3] ),
                    TestEntry( rating = [1,2,3,4] ),
                ]

    # expected output:
    '''
    3
    0
    4
    '''

    for t in test_data:

        print( Solution().numTeams( rating = t.rating ) )
    
    return



if __name__ == '__main__':

    test_bench()
