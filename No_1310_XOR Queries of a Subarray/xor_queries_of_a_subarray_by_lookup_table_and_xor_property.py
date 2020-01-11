'''

Description:

Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.
 

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]
 

Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 10^9
1 <= queries.length <= 3 * 10^4
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] < arr.length

'''




# XOR property review:
'''
Associativity:
(A XOR B) XOR C = A XOR (B XOR C)

Commutativity:
A XOR B = B XOR A

Idempotency:
A XOR A = 0
'''


from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        result, size  = [], len(arr)
        
        look_up_table = [0] * ( size+1 )
        
        
        # table[i] = arr[0] XOR arr[1] XOR ... XOR arr[i-1]
        for i in range(size):
            look_up_table[i+1] = look_up_table[i] ^ arr[i]
        
        
        
        # compute query, q, by look-up table as well as XOR property
        '''
        Left = ( prefix leading temrs ) 
        Right = ( prefix leading temrs ) XOR arr[ q[0] ] XOR ... XOR arr[ q[1] ]
        
        Left XOR Right = arr[ q[0] ] XOR ... XOR arr[ q[1] ]
        '''
        for q in queries:
            left = look_up_table[ q[0] ]    
            right = look_up_table[ q[1] + 1 ]
            result.append( left ^ right )
            
            
        
        return result



# n : the length of input list, arr.
# q : the length of input list, queries.

## Time Complexity: O( n + q )
#
# The overhead in time is the for loop iterating on i of O( n ), and the for loop iterating on q of O( q )
# It takes O( n + q ) in total.



## Space Complexity: O( n )
#
# The overhead in space is the storage for look-up talbe, which is of O( n ).



def test_bench():

    test_data = [
                    ( [1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]  ),
                    ( [4,8,2,10], [[2,3],[1,3],[0,0],[0,3]] )
                ]

    # expected output:

    '''
    [2, 7, 14, 8]
    [8, 0, 4, 4]
    '''


    for arr, queries in test_data:

        print( Solution().xorQueries( arr, queries) )

    return 



if __name__ == '__main__':

    test_bench()