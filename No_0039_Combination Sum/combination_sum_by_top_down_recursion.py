'''

Description:

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
	[7],
	[2,2,3]
]



Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
	[2,2,2,2],
	[2,3,3],
	[3,5]
]

'''



from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # preprocessing, sort candidates in ascending order
        candidates.sort()

        # record of minimum element in candidates
        mini = candidates[0]

        # record the valid combination
        result = []

        def combination_find(target, start, end, path):

            if target == 0:
                # path sum equals to target, find one valid combination
                result.append(path)
                return 

            for i in range(start, end + 1):
                cur = candidates[i]
                
                if cur > target:
                    # pruning:
                    # current minimum element is larger that target
                    # impossible to make combination
                    break

                remaining = target - cur

                if remaining and remaining < mini: 
                    # remainder is smaller than smallest number in candidates
                    continue
            
                # DFS search:
                combination_find(remaining, i, end, path + [cur])

        # DFS search
        combination_find(target, 0, len(candidates) - 1, [])
        return result



# n : the length of candidates
# t : the value of target

## Time Complexity: O( n * 2 ^ n )
#
# The overhead in time is the cost of dfs, which is of O( n * 2 ^ n )

## Space Complexit: O( t )
#
# The overhead in space is the storage for recursion call stack, which is of O( t )


def test_bench():

	test_data = [
									([2,3,6,7], 7),
									([2,3,5], 8)
							]

	for candidates, target in test_data:

			print( Solution().combinationSum(candidates, target) )
	
	return



if __name__ == '__main__':

	test_bench()