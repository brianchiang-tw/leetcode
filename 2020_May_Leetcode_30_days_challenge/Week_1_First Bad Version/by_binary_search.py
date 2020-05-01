'''

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

'''




# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

product_status = None

def isBadVersion(version):
    global product_status
    return product_status[version-1] == 'x'

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left, right = 1, n
        
        while left <= right:
            
            mid = left + (right-left)//2
            
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return (right+1)



# n : the length of input parameter

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search from 1 to n, which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for index of binary search, which is of O( 1 )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'product_status')
def test_bench():

    test_data = [
                    TestEntry( product_status = ['o','o','o','x','x'] ),
                    TestEntry( product_status = ['o','o','o','o','x'] ),
                    TestEntry( product_status = ['o','o','x','x','x'] ),
                    TestEntry( product_status = ['o','x','x','x','x'] ),
                    TestEntry( product_status = ['x','x','x','x','x'] ),
                ]



    # expected output:
    '''
    4
    5
    3
    2
    1
    '''

    global product_status

    for t in test_data:

        product_status = t.product_status

        print( Solution().firstBadVersion( n = len(product_status) ) )

    return



if __name__ == '__main__':

    test_bench()