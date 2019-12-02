'''

Description:

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

 

Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
 

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

'''

import threading
from time import sleep



class Foo:
    def __init__(self):
        self.running_token = 1
        
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        while self.running_token != 1:
            sleep( 0.0001 )
        
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.running_token = 2

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        while self.running_token != 2:
            sleep( 0.0001 )
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.running_token = 3

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        while self.running_token != 3:
            sleep( 0.0001 )
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


## Time Complexity: O( 1 )
#
# The overhead is the token busy waiting loop, the number of busy waiting loop is constant.

## Space Complexity: O( 1 )
#
# The overhead is the token variable, which is of O( 1 )



# def printFirst():

#     print("first", end = '')
#     return

# def printSecond():

#     print("second", end = '')
#     return

# def printThird():

#     print("third", end = '')
#     return



# def worker_thread( instance, function_serial_number ):

#     # function dispatcher
#     if 1 == function_serial_number:
#         instance.first( printFirst )

#     elif 2 == function_serial_number:
#         instance.second( printSecond )

#     elif 3 == function_serial_number:
#         instance.third( printThird )
    
#     return



# def test_bench():

#     test_data = [
#                     [1,2,3],
#                     [1,3,2],
#                     [3,2,1]
#                 ]


#     # expected output:
#     '''
#     firstsecondthird
#     firstsecondthird
#     firstsecondthird
#     '''


#     for test in test_data:

#         # create an instance of class Foo
#         instance_of_Foo = Foo()

#         # a container for threads
#         thread_pool = [None]*3

#         for i in range( len(test) ):
#             # create 3 different threads
#             thread_pool[i] = threading.Thread(name='worker'+str( test[i] ), target=worker_thread, args=(instance_of_Foo, test[i]) )

#         for i in range( len(test ) ):
#             # let thread_i start running
#             thread_pool[i].start()
            
#         sleep(5)
#         print()

#     return



# if __name__ == '__main__':

#     test_bench()