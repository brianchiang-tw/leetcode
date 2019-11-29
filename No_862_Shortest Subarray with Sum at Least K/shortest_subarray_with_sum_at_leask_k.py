''''

Description:

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9

'''


import collections
class Solution(object):

    def shortestSubarray( self, A, K):

        size = len(A)

        # sub_sum denotes as S
        sub_sum = [ 0 ]

        # update sub_sum
        # S[ 1 ] = A[ 0 ]
        # S[ 2 ] = A[ 0 ] + A[ 1 ]
        # S[ 3 ] = A[ 0 ] + A[ 1 ] + A[ 2 ]

        for element in A:
            sub_sum.append( sub_sum[-1] + element )

        queue = collections.deque()    
        range_length = ( size + 1 )



        for i in range(size+1):

            while queue and sub_sum[i] <= sub_sum[ queue[-1] ]:
                queue.pop()

            while queue and ( sub_sum[i] - sub_sum[ queue[0] ] ) >= K:
                range_length = min( range_length, i - queue.popleft() )

            queue.append( i )


        return range_length if range_length < (size + 1) else -1 




'''

class Solution(object):
    def shortestSubarray(self, A, K):
 
        n, dp = len(A), [0]  # 初始化dp[i] = A[0]+A[1]+...+A[i-1]
        for v in A: dp.append(dp[-1] + v)
 
        queue, res = collections.deque(), n + 1  # 初始化队列、结果变量
        for i in range(n+1):
            while queue and dp[i] <= dp[queue[-1]]:
                queue.pop()  # 出队, 删除不符合的
 
            while queue and dp[i] - dp[queue[0]] >= K:
                res = min(res, i - queue.popleft())  # 从左边出队，并更新最短距离。
 
            queue.append(i)  # 入队
 
        return res if res < n + 1 else -1  #返回最优解

'''
