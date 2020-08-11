'''

Description:

Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:


Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.

 

Example 1:


Input: n = 7, cuts = [1,3,4,5]
Output: 16
Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:

The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).



Example 2:

Input: n = 9, cuts = [5,6,1,4,2]
Output: 22
Explanation: If you try the given cuts ordering the cost will be 25.
There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.
 

Constraints:

2 <= n <= 10^6
1 <= cuts.length <= min(n - 1, 100)
1 <= cuts[i] <= n - 1
All the integers in cuts array are distinct.

'''


from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        ## dictionary:
        # key: cut index pair
        # value: minimum cutting cost
        cost_dict = {}
        
        ## initialization
        # adding end points and keep cut point sorted in ascending order
        cuts = [0] + sorted(cuts) + [n]
        
        # -------------------------------------------------------------------------
        def cutter(left_cut_index, right_cut_index):
            
            if (left_cut_index, right_cut_index) in cost_dict:
                # Quick response with memoization
                return cost_dict[ (left_cut_index, right_cut_index) ]
            
            left_boundary = cuts[left_cut_index]
            right_boundary = cuts[right_cut_index]
            
            if (right_boundary - left_boundary) <= 1:
                # Base case:
                # current stick is with either length 0 or length 1 stick
                # no need to cut
                return 0
            
            elif (right_cut_index - left_cut_index) <= 1:
                # Base case:
                # No cutting point exists in interval [left_boundary, right_boundary]
                return 0
            
            else:
                # General case:
                # At least one cutting point exists in interval [left_boundary, right_boundary]
                cost_of_range = float('inf')
            
                # Solve by Dynamic Programming with memoziation
                for cut_index in range(left_cut_index+1, right_cut_index):

                    cost_of_trial = cutter(left_cut_index, cut_index) + cutter(cut_index, right_cut_index)
                    
                    # update with minimum cost
                    cost_of_range = min(cost_of_range, cost_of_trial)
                
        
                cost_of_cut_cur_length = right_boundary - left_boundary
                total_cost = cost_of_cut_cur_length + cost_of_range
                
                cost_dict[ (left_cut_index, right_cut_index) ] = total_cost
                
                return total_cost
        # -------------------------------------------------------------------------
        
        return cutter(left_cut_index=0, right_cut_index=len(cuts) - 1)  



# n : the length of stick

## Time Complexity: O( n^3)
#
# The overhead in time is the cost of nested iteration with three indices, which is of O( n^3 )

## Space Complexity: O( n^2 )
#
# The overhead in time is the storage for dictionary, which is of O( n^2 )



import unittest


class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().minCost(n = 7, cuts = [1,3,4,5])
        self.assertEqual(result, 16)

    
    def test_case_2(self):
    
        result = Solution().minCost(n = 9, cuts = [5,6,1,4,2])
        self.assertEqual(result, 22)


if __name__ == '__main__':

    unittest.main()