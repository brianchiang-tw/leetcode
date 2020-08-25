'''

Description:

We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].



Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000

'''



class Solution(object):
    def distributeCandies(self, candies, num_people):


        n = num_people
        
        # candies distribution for each person
        result = [0] * n
         
        c = 0
        while candies > 0:
            
            # candies may be not enough on last round, therefore compute min(candies, c+1)
            result[c % n] += min(candies, c+1)
            
            # add one more candies for next person
            c += 1
            
            # update total number of candies
            candies -= c
        
        return result


# n : the value of input, candies
# m : the value of input, num_of_people

## Time Complexity: O( sqrt(n) )
#
# The overhead in time is the cost of while iteration, which is of O( sqrt(n) )

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, which is of O( m )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):
        result = Solution().distributeCandies( candies = 7, num_people = 4 )
        self.assertEqual( result, [1,2,3,1] )


    def test_case_2( self ):
        result = Solution().distributeCandies( candies = 10, num_people = 3 )
        self.assertEqual( result, [5,2,3] )




if __name__ == '__main__':

    unittest.main()