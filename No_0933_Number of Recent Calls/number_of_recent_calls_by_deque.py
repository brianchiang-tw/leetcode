
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


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



# t : the calling time of input ping()

## Time Complexity:
#
# The major overhead in time is the while loop iterating in self.call_queue[0] < t-3000, which is of O(t)


## Space Complexity: O( 1 )
#
# The major overhead in space is the storage for call_queue, which is of O( 3000 ) = O( 1 )



def test_bench():

    test_data = [1, 100, 3001, 3002]

    call_record = RecentCounter()

    # expected output:
    '''
    1
    2
    3
    3
    '''


    for calling_time in test_data:

        print( call_record.ping( calling_time ) )

    return 



if __name__ == '__main__':

    test_bench()

    

