'''

Description:

We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)

Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.

 

Example 1:

Input: ["cba","daf","ghi"]
Output: 1
Explanation: 
After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
Example 2:

Input: ["a","b"]
Output: 0
Explanation: D = {}
Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: D = {0, 1, 2}
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 1000

'''



from typing import List
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        # transpose A to get column pair
        column_pair = list( zip( *A ) )
        
        # a set to collect index of out-of-order column
        column_mismatch = set()
        
        # check each column
        for col_i, pair in enumerate(column_pair):
            
            # check the property of non-decreasing: pair[j] <= pair[j+1] for every j
            for j in range( len(pair)-1 ):
                
                if pair[j] > pair[j+1]:
                    
                    # column is out-of-order
                    column_mismatch.add(col_i)
                    break
        
        
        return len( column_mismatch )


# m : the length of word in A

# n : the length of input list, A.

## Time Complexity: O( m * n )
#
# The overhead in time is the dimension of word matrix, which if O( m * n )

## Space Complexity: O( m )
#
# The overhead in space is the storage for set, column_mismatch, which is of O( m )


def test_bench():

    test_data = [
                    ["cba","daf","ghi"],
                    ["a","b"],
                    ["zyx","wvu","tsr"]
                ]
    
    # expected output:
    '''
    1
    0
    3
    '''


    for test_list in test_data :

        print( Solution().minDeletionSize( test_list ) )
    
    return 



if __name__ == '__main__':

    test_bench()