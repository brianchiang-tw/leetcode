'''

Description:

Suppose you are given the following code:

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // constructor
  public void zero(printNumber) { ... }  // only output 0's
  public void even(printNumber) { ... }  // only output even numbers
  public void odd(printNumber) { ... }   // only output odd numbers
}
The same instance of ZeroEvenOdd will be passed to three different threads:

Thread A will call zero() which should only output 0's.
Thread B will call even() which should only ouput even numbers.
Thread C will call odd() which should only output odd numbers.
Each of the threads is given a printNumber method to output an integer. Modify the given program to output the series 010203040506... where the length of the series must be 2n.

 

Example 1:

Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously. One of them calls zero(), the other calls even(), and the last one calls odd(). "0102" is the correct output.



Example 2:

Input: n = 5
Output: "0102030405"

'''



from threading import Lock
from threading import Thread
from time import sleep
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        
        self.zero_mutex = Lock()
        self.odd_mutex = Lock()
        self.even_mutex = Lock()
        
        # Lock mutex for even number and odd number, 
        # because 0 must be printed first
        self.even_mutex.acquire()
        self.odd_mutex.acquire()
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        
        for i in range(1, self.n+1):

            # lock mutex for zero
            self.zero_mutex.acquire()
            
            printNumber(0)
            

            if ( i % 2 )== 1:
                # unlock mutex for odd number
                self.odd_mutex.release()
            else:
                # unlock mutex for even number
                self.even_mutex.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        
        for j in range(2, self.n+1, 2):

            # lock mutex for even number
            self.even_mutex.acquire()
            
            printNumber(j)
            
            # unlock mutex for zero
            self.zero_mutex.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        
        for k in range(1, self.n+1, 2):
            
            # lock mutex for odd number
            self.odd_mutex.acquire()
            
            printNumber(k)
            
            # unlock mutex for zero
            self.zero_mutex.release()



# n : the input value in the constructor (i.e., __init__() ) of ZeroEvenOdd

## Time Complexity: O( n )
#
# The overhead in time is the looping length, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the mutex for zero, odd, and even, as well as the looping index, which is of O( 1 )



def printNumber( x: int):

    print(f'{x}', end = '')
    return



def worker_thread( instance, function_serial_number ):

    # function dispatcher
    if 1 == function_serial_number:
        instance.zero( printNumber )

    elif 2 == function_serial_number:
        instance.even( printNumber )

    elif 3 == function_serial_number:
        instance.odd( printNumber )
    
    return



def test_bench():

    test_data = [
                    (10, [1,2,3]),
                    (15, [1,2,3]),
                    (20, [1,2,3])
                ]


    # expected output:
    '''
    010203040506070809010
    010203040506070809010011012013014015
    010203040506070809010011012013014015016017018019020
    '''


    for n, thread_sequence in test_data:

        # create an instance of class Foo
        instance_of_NumberCounter = ZeroEvenOdd(n)

        # a container for threads
        thread_pool = [None]*3

        for i in range( len(thread_sequence) ):
            # create 3 different threads
            thread_pool[i] = Thread(name='worker'+str( thread_sequence[i] ), target=worker_thread, args=(instance_of_NumberCounter, thread_sequence[i]) )

        for i in range( len(thread_sequence ) ):
            # let thread_i start running
            thread_pool[i].start()
            
        for i in range( len(thread_sequence ) ):
            # let thread_i start running
            thread_pool[i].join()
        
        # idle one second
        sleep(1)
        print()

    return



if __name__ == '__main__':

    test_bench()