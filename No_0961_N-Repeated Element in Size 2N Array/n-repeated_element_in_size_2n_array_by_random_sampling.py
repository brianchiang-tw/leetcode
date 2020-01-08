'''

Description:

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even

'''



from random import sample
from typing import List
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        while True:
        
            x, y = sample(A, 2)
            
            if x == y:
                return x



# n : the length of input list, A.

## Time Complexity: O( 1 )
#
# The overhead in time is the expectation of hit the same number = 1 / C(n,2)/C(2n,2), which is of O( 4 ) as n grows

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for random sampling, ( x, y), which is of ( n )



def test_bench():

    test_data = [
                    [1,2,3,3],
                    [2,1,2,5,3,2],
                    [5,1,5,2,5,3,5,4]
                ]

    for test_seq in test_data:

        print( Solution().repeatedNTimes(test_seq) )

    return 



if __name__ == '__main__':

    test_bench()