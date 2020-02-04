'''

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

'''



from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        # list comprehension
        list_of_output = [ 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5 ) or str(i) for i in range(1, n+1) ]
        
        return list_of_output



# n : the input value

## Time Complexity: O( n )
# The overhead in time is the list comprehension's for loop iterating on i, which is of O( n )


## Space Complexity: O( n )
#
# The overhead in space is the storage for list_of_output, which is of O( n )



def test_bench():

    test_data = [ 1, 3, 5, 6, 10, 12, 15 ]
                    
    # expected output:
    '''
    ['1']
    ['1', '2', 'Fizz']
    ['1', '2', 'Fizz', '4', 'Buzz']
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz']
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz']
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    '''


    for number in test_data:

        print( Solution().fizzBuzz(number) )
    
    return



if __name__ == '__main__':

    test_bench()
                