from collections import defaultdict
from bisect import insort_left, bisect_left
from typing import List
class TweetCounts:

    def __init__(self):

        # dictionary:
        # key   : tweetname
        # value : list of timestamps
        self.tweet_timestamp = defaultdict( list )            

        
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        
        # insert new timestamp for tweetName, and keep in order
        insort_left( self.tweet_timestamp[tweetName], time )

        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        arr_timestamp = self.tweet_timestamp[tweetName]
        
        unit_size = None
        
        # compute unit size from given frequency
        if freq == 'minute':
            unit_size = 60
        elif freq == 'hour':
            unit_size = 60 * 60
        elif freq == 'day':
            unit_size = 60 * 60 * 24
        
        # compute total number of intervals
        num_of_interval = (endTime - startTime)//unit_size + 1
        
        # list for output
        result = [ 0 for i in range(num_of_interval) ]
        
        # find the index of first timestamp in query range
        index = bisect_left(arr_timestamp, startTime)
        
        # update statistics of tweet occurrences based on specified interval
        while index < len(arr_timestamp) and arr_timestamp[index] <= endTime:
            result[ (arr_timestamp[index]-startTime) // unit_size ] += 1
            index += 1
            
        return result


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)



# n : the number of operation
# q : maximum query interval

## Time Complexity
# For recordTweet(), 
# each time it takes O( log n ) to insert a element at most.
# 
# For getTweetCountsPerFrequency(),
# each time it takes O( q ) to collect and compute frequenct in given query range.



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'operation parameter')
def test_bench():

    test_data = [
                    TestEntry('record_tweet', ("tweet3", 0) ),
                    TestEntry('record_tweet', ("tweet3", 60) ),
                    TestEntry('record_tweet', ("tweet3", 10) ),
                    TestEntry('query', ("minute", "tweet3", 0, 59) ),
                    TestEntry('query', ("minute", "tweet3", 0, 60) ),
                    TestEntry('record_tweet', ("tweet3", 120) ),
                    TestEntry('query', ("hour", "tweet3", 0, 120) ),
                ]

    instance = TweetCounts()

    for t in test_data:

        if t.operation == 'record_tweet':
            instance.recordTweet( *(t.parameter) )

        elif t.operation == 'query':
            print( instance.getTweetCountsPerFrequency( *(t.parameter) ) )
    
    return



if __name__ == '__main__':

    test_bench()