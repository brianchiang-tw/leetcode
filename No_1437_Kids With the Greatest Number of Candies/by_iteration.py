'''

Description:

Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

 

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: 
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 



Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.



Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
 

Constraints:

2 <= candies.length <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50

'''



from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result, maximum = [], max( candies )
        
        for candy in candies:
            
            # check whether currnet kid can achieve maximum by adding extra candies
            if (candy + extraCandies) >= maximum:
                result.append( True )
            
            else:
                result.append( False )
                
        return result



# n : the length of input array, candies.

## Time Complexity: O( n )
#
# The overhead in time is the cost of maximum finding and for loop iteration, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output array, result, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'candy_sequence extra_candies')

def test_bench():

    test_data = [
                    TestEntry( candy_sequence = [2,3,5,1,3], extra_candies = 3 ),
                    TestEntry( candy_sequence = [4,2,1,1,2], extra_candies = 1 ),
                    TestEntry( candy_sequence = [12,1,12], extra_candies = 10 ),
                ]
    
    # expected output:
    '''
    [True, True, True, False, True]
    [True, False, False, False, False]
    [True, False, True]
    '''

    for t in test_data:

        print( Solution().kidsWithCandies( candies = t.candy_sequence, extraCandies = t.extra_candies) )
    
    return



if __name__ == '__main__':

    test_bench()