'''

Description:

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

 

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     # requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   # requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  # requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 

Constraints:

1 <= t <= 109
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.

'''


from collections import deque

class RecentCounter:

    def __init__(self):
        
        # a double-ended queue that keep fresh calls in math interval [t-3000, t]
        self.call_queue = deque()



    def ping(self, t: int) -> int:
        
        # pop out-of-date calls which calling time is smaller than t-3000 on the front
        while self.call_queue and self.call_queue[0] < t-3000:    
            self.call_queue.popleft()
        
        
        # push in-coming call on the rear
        self.call_queue.append(t)
        
        
        return len(self.call_queue)


# Time Complexity: O( 1 )
#
# The overhead in time is the cost of maintin a O( 3000 ) deque, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for O( 3000 ) deque, which is of O( 1 )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        recentCounter = RecentCounter()

        result = recentCounter.ping(1)       # requests = [1], range is [-2999,1], return 1
        self.assertEqual(result, 1)

        result = recentCounter.ping(100)     # requests = [1, 100], range is [-2900,100], return 2
        self.assertEqual(result, 2)


        result = recentCounter.ping(3001)    # requests = [1, 100, 3001], range is [1,3001], return 3
        self.assertEqual(result, 3)

        result = recentCounter.ping(3002)    # requests = [1, 100, 3001, 3002], range is [2,3002], return 3
        self.assertEqual(result, 3)



if __name__ == '__main__':

    unittest.main()
        