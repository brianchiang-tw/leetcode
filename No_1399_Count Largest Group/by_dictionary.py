'''

Description:

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.



Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.



Example 3:

Input: n = 15
Output: 6



Example 4:

Input: n = 24
Output: 5
 

Constraints:

1 <= n <= 10^4

'''



from collections import defaultdict

class Solution:
    
    def digitsum( self, x ):
        
        s = 0
        
        while x:
            q, r = divmod( x, 10)
            s += r
            x = q
        
        return s
    
    
    
    def countLargestGroup(self, n: int) -> int:
        
        digitsum_num_dict = defaultdict( list )
        
        for number in range(1,n+1):
        
            digit_sum = self.digitsum( number )
            
            digitsum_num_dict[digit_sum].append( number )
            
            
        max_size, max_grp_cnt = 0, 0
        
        for digitsum in digitsum_num_dict:
            
            cur_size = len( digitsum_num_dict[digitsum] )
            if cur_size > max_size:
                max_size = cur_size
                max_grp_cnt = 1
            
            elif cur_size == max_size:
                max_grp_cnt += 1
                
        
        return max_grp_cnt



# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the cost of loop, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, digitsum_num_dict, which is of o( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'n')
def test_bench():

    test_data = [
                    TestEntry( n = 13),
                    TestEntry( n = 2),
                    TestEntry( n = 15),
                    TestEntry( n = 24),
                    TestEntry( n = 1),
                    TestEntry( n = 1000),
                ]

    # expected output:
    '''
    4
    2
    6
    5
    1
    2
    '''
    for t in test_data:
        print( Solution().countLargestGroup( n = t.n ) )

    return



if __name__ == '__main__':

    test_bench()