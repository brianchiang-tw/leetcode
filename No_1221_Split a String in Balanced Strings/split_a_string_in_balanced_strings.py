class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        size = len(s)
        max_balanced_pair_count = 0

        for i in range( size):
            
            if s[0:i+1].count('L') == s[0:i+1].count('R'):
                
                # update max balance pair count
                max_balanced_pair_count += 1

        return max_balanced_pair_count


# n : the length in input string

## Time Complexity: O( n )
#
# The overhead in time is the for loop itertaions, which is of O( n )

## Space Complexity: O( 1 )
#
# The oberhead in space is to maintain variable for counter, which is of O( 1 )


def test_bench():

    test_data = ["RLRRLLRLRL"]

    for s in test_data:

        print( Solution().balancedStringSplit(s) )



if __name__ == '__main__':

    test_bench()