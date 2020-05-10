'''

Description:

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2



Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3



Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1



Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1



Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

'''


from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N == 1:
            # Quick response for small case
            return 1
        
        
        trust_score = [ 0 for _ in range(N+1) ]
        
        for p1, p2 in trust:
            
            # decrease one point from p1 when p1 trust other people
            trust_score[p1] -=1
            
            # increase one point to p2 when p2 is trusted by others
            trust_score[p2] +=1
            
            
        
        for person in range(1, N+1):
            
            # town judge will be trusted by other N-1 people, and town judge trust nobody.
            if trust_score[person] == N-1:
                return person
        
        return -1



# n : the input value of N
# t : the length of input list, trust.

## Time Complexity: O(t+n)
#
# The overhead in time is the cost of first loop of O(t), and the cost of second loop of O(n).
# It takes O(t+n) in total.

## Space Complexity: O( n )
#
# The overhead in sapce is the storage for table, trust_score, which is of O( n ).

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'N trust_relationship')

def test_bench():

    test_data = [
                    TestEntry( N = 2, trust_relationship = [[1,2]] ),
                    TestEntry( N = 3, trust_relationship = [[1,3],[2,3]] ),
                    TestEntry( N = 3, trust_relationship = [[1,3],[2,3],[3,1]] ),
                    TestEntry( N = 3, trust_relationship = [[1,2],[2,3]] ),
                    TestEntry( N = 4, trust_relationship = [[1,3],[1,4],[2,3],[2,4],[4,3]] ),
                ]        

    # expected output:
    '''
    2
    3
    -1
    -1
    3
    '''

    for t in test_data:

        print( Solution().findJudge( N = t.N, trust = t.trust_relationship) ) 

    return



if __name__ == '__main__':

    test_bench()                   