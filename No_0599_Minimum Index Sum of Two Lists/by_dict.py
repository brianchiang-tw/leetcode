'''

Description:

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

Output: ["Shogun"]

Explanation: The only restaurant they both like is "Shogun".



Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]

Output: ["Shogun"]

Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.

'''


from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        restaurant_idx_dict_1 = { rest : idx for idx, rest in enumerate(list1) }
        restaurant_idx_dict_2 = { rest : idx for idx, rest in enumerate(list2) }
        
        # itersection set of dict_1 and dict_2
        common_rest = restaurant_idx_dict_1.keys() & restaurant_idx_dict_2.keys()
        
        if len(common_rest) == 1:
            
            # single element in intersection
            
            return [ common_rest.pop() ]
    
        else:
            
            # multiple elements in intersection
            
            min_idx_sum = (1000-1)*2
            optimal_restaurant = []
            for r in common_rest:
                
                cur_idx_sum = restaurant_idx_dict_1[ r ] + restaurant_idx_dict_2[ r ]
                
                if cur_idx_sum < min_idx_sum:
                    optimal_restaurant.clear()
                    
                    min_idx_sum = cur_idx_sum
                    optimal_restaurant.append( r )
                
                elif cur_idx_sum == min_idx_sum:
                    
                    optimal_restaurant.append( r )
                
            return optimal_restaurant
                


# m : the length of input list1
# n : the length of input list2

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of dictionary building, and minimum index sum update, which are of O( m + n ).

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for dictionaries, which are of O( m + n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'list1 list2')

def test_bench():

    test_data = [
                    TestEntry( list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"], list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"] ),
                    TestEntry( list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"], list2 = ["KFC", "Shogun", "Burger King"] ),
                ]

    # expected output:
    '''
    ['Shogun']
    ['Shogun']
    '''

    for t in test_data:
        print( Solution().findRestaurant( list1 = t.list1, list2 = t.list2 ) )    

    return



if __name__ == '__main__':

    test_bench()