'''

Description:

Implement the class ProductOfNumbers that supports two methods:

1. add(int num)

Adds the number num to the back of the current list of numbers.
2. getProduct(int k)

Returns the product of the last k numbers in the current list.
You can assume that always the current list has at least k numbers.
At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 

Example:

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
 

Constraints:

There will be at most 40000 operations considering both add and getProduct.
0 <= num <= 100
1 <= k <= 40000

'''



class ProductOfNumbers:

    def __init__(self):
        
        self.product_table = [1]
        
    def add(self, num: int) -> None:
        
        if num != 0:
            # update product table if num is non-zero.
            self.product_table.append( num * self.product_table[-1] )
        else:
            # reset product table after 0 is insert
            self.product_table = [1]

            
            
    def getProduct(self, k: int) -> int:
        
        if k >= len( self.product_table ):
            # this query with last k will meet 0, which was inserted before getProduct() query
            return 0
        else:
            # compute the product of last k elemetns by look-up table
            return self.product_table[-1] // self.product_table[-(k+1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)



# n : the number of operations 

## Time Complexity : O( 1 ) 
#
# For add():
# It takes O(1) to update the accumulation product with the previous one.
#
# For getProduct():
# It takes O(1) for condition judgement, as well as compute and return table lookup value.


## Space Complexity : O( n )
#
# For add():
# Single add takes O(1), and there are total O( n ) non-zero numbers in product_table at most.
#
# For getProduct():
# It takes O( 1 ) for condition judgement, as well as compute and return table lookup value.



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'operation value')

def test_bench():


    # expected output:
    '''
    20
    40
    0
    32
    '''
    instance = ProductOfNumbers()

    test_data = [
                    TestEntry('add', 3),
                    TestEntry('add', 0),
                    TestEntry('add', 2),
                    TestEntry('add', 5),
                    TestEntry('add', 4),
                    TestEntry('query_product', 2),
                    TestEntry('query_product', 3),
                    TestEntry('query_product', 4),
                    TestEntry('add', 8),
                    TestEntry('query_product', 2)
                ]

    for t in test_data:

        if t.operation == 'add':
            instance.add( t.value )
        elif t.operation == 'query_product':
            print( instance.getProduct( t.value) )

    return



if __name__ == '__main__':

    test_bench()