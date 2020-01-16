'''

Description:

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True



Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False



Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.

'''



from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        
        size = len(flowerbed)
        
        if n == 0:
            # n = 0, no need to plant
            return True
        
        if size == 1:
            # corner case handle:
            if flowerbed[0] == 0 and n <= 1:
                return True
            if flowerbed[0] == 1 and n != 0:
                return False
            
                
        
        count_of_plant = 0
        
        for index in range(size):
            
            if count_of_plant == n:
                # n flowers are planted already
                break
            
            if index == 0:
                # the first position
                if flowerbed[index] == 0 and flowerbed[index+1] != 1:
                    flowerbed[index] = 1
                    count_of_plant += 1
                    
            elif index == size-1:
                # the last position
                if flowerbed[index] == 0 and flowerbed[index-1] != 1:
                    flowerbed[index] = 1
                    count_of_plant += 1
            
            else:
                # position in the middle
                if flowerbed[index] == 0 and flowerbed[index-1] != 1 and flowerbed[index+1] != 1:
                    flowerbed[index] = 1
                    count_of_plant += 1
        
        
        return count_of_plant == n



# n : the length of input list, flowerbed.

## Time Complexity: O( n )
#
# The overhead in time is the while loop iterating on index, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and flower counter, which is of O( 1 ).


def test_bench():

    test_data = [
                    ([1,0,0,0,1], 1),
                    ([1,0,0,0,1], 2),
                    ([0,0,0,0,0], 1),
                    ([0,0,0,0,0], 2),
                    ([0,0,0,0,0], 3),
                    ([0,0,0,0,0], 4),
                    ([0,0,0,0,0], 5)
                ]

    # expected output:
    '''
    True
    False
    True
    True
    True
    False
    False
    '''


    for flowerbed, n in test_data:

        print( Solution().canPlaceFlowers(flowerbed, n) )
    
    return 



if __name__ == '__main__':

    test_bench()