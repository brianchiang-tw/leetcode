'''

Description:

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].



Hint #1  
Try to represent the current (N, K) in terms of some (N-1, prevK). What is prevK ?

'''



class Solution:
    def kthGrammar(self, N: int, K: int) -> int:

        if N == 1:
            return 0

        else:

            if K % 2 == 0:
                return 0 if self.kthGrammar( N-1, (K+1)//2 ) else 1
            else:
                return 1 if self.kthGrammar( N-1, (K+1)//2 ) else 0



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'N K')

def test_bench():

    test_data = [
                    TestEntry( N = 1, K = 1 ),
                    TestEntry( N = 2, K = 1 ),
                    TestEntry( N = 2, K = 2 ),
                    TestEntry( N = 4, K = 5 ),
                ]

    # expected output:
    '''
    0
    0
    1
    1
    '''

    for t in test_data:

        print( Solution().kthGrammar( *t ) )
    

    return



if __name__ == '__main__':

    test_bench()