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



from collections import defaultdict
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        sum_element_dict = defaultdict( set )
        
        min_value = 2 ** 31 
        for element in candidates:
            
            min_value = min(min_value, element)
            sum_element_dict[element].add(  (element,) ) 
        
        if target < min_value:
            # Quick response
            # If target < minimal value of candidates, then there is no solution
            return []
        
        
        for number in range( min_value, target+1):
            
            for element in candidates:
                
                gap_value = (number-element)
                if gap_value in sum_element_dict:
                    
                    combination_gap_value = sum_element_dict[gap_value]
                    
                    for c in combination_gap_value:
                        
                        cur_combination = c + (element,)
                        
                        list_of_cur_comb = list(cur_combination)
                        list_of_cur_comb.sort()
                        cur_combination = tuple( list_of_cur_comb )
 
                        sum_element_dict[ number ].add( cur_combination )
        
        
        
        if target in sum_element_dict:
            combination_of_target = list( map( list, sum_element_dict[ target ] ) )    
            return combination_of_target
        
        else:
            return []



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