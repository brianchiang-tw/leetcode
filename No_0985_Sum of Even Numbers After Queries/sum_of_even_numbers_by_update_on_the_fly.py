'''

Description:

We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

 

Example 1:

Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: 
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length

'''



from typing import List
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        
        # a list to store sum of even numbers
        sum_of_even = []
        
        cur_sum_of_even = sum( element for element in A if element % 2 == 0)
        
        # check each query
        for q in queries:
            
            # get index and offset from single query q
            offset, index = q
            
            # derease current sum of even by old even number 
            if A[index] % 2 == 0:
                cur_sum_of_even -= A[index]
            
            # update A[index] with offset
            A[index] += offset
            
            # increase current sum of even by new even number 
            if A[index] % 2 == 0:
                cur_sum_of_even += A[index]
            
            # push current sum of even to list
            sum_of_even.append( cur_sum_of_even )
            
        
        return sum_of_even  



# n : the length of input list, A.
# q : the length of input queries.

## Time Complexity: O( n + q )
#
# The overhead in time is the sum( ... ) of A, which is of O( n ), and 
# the for loop iterating on queries, which is of O( q ).


## Space Complexity: O( q )
# 
# The overhead in storage is the list for output, sum_of_even, which is of O( q ).


def test_bench():

    test_data = [
                    ( [1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]] ),
                    ( [1,3,5,7], [[1,0],[-3,1],[-4,0],[2,3]] )
                ]

    # expected output:
    '''
    [8, 6, 2, 4]
    [2, 2, -2, -2]    
    '''

    for arr, queries in test_data:
        
        print( Solution().sumEvenAfterQueries( A = arr, queries = queries ) )

    return 



if __name__ == '__main__':

    test_bench()