'''

Description:

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    
    def permuteUnique(self, num):
        length = len(num)
        if length == 0: return []
        if length == 1: return [num]
        
        # pre-processing
        
        num.sort()
        res = []
        previousNum = None
        for i in range(length):
            if num[i] == previousNum: continue
            previousNum = num[i]
            for j in self.permuteUnique(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        return res


def test_bench():

    test_data = [1,1,2]

    print( Solution().permuteUnique(test_data) )

    return



if __name__ == '__main__':

    test_bench()