'''

Description:

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.



Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.



Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
 

Constraints:

0 <= arr.length <= 105
-109 <= arr[i] <= 109

'''



from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        # keep unique elements of array in ascending order
        elements_ascending = sorted(set(arr))
        
        # dictionary
        # key   : number
        # value : rank
        num_rank_dict = dict()
        

        for index, num in enumerate(elements_ascending):
            
            # rank = index + 1
            num_rank_dict[num] = (index+1)
                
        
        # give each number with its corresponding rank
        result = [ num_rank_dict[num] for num in arr ]
        
        return result



# n : the length of input array, arr.
# k : the number of unique elements of arr.


## Time Complexity: O( k log k + n )
#
# The overhead in time is the sort for unique elements, which is of O( k log k ),
# and the cost of list comprehension over arr, which is of O( n ).
#
# It takes O( k log k + n ) in total.


## Space Complexity: O( k + n ) = O( n )
#
# The overhead in space is the storage for dictionary, num_rank_dict, which is of O( k ),
# and for list comprehension, result, which is of O( n ).
#
# It takes O( k + n ) = O( n ) in total.



def test_bench():

    test_data = [
                    [40,10,20,30],
                    [100,100,100],
                    [37,12,28,9,100,56,80,5,12]
                ]

    # expected output:
    '''
    [4, 1, 2, 3]
    [1, 1, 1]
    [5, 3, 4, 2, 8, 6, 7, 1, 3]    
    '''

    for sequence in test_data:
        
        print( Solution().arrayRankTransform(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()