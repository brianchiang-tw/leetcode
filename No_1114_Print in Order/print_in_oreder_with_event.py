from threading import Event
from time import sleep



class Foo:
    def __init__(self):
        
        #self.evt_1_ready = Event()
        self.evt_2_ready = Event()
        self.evt_3_ready = Event()
        
        #self.evt_1_ready.set()
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        #self.evt_1_ready.wait()
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        
        self.evt_2_ready.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.evt_2_ready.wait()
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.evt_3_ready.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.evt_3_ready.wait()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


## Time Complexity: O( 1 )
#
# The overhead is the event wait and set, the number of event loop is constant.

## Space Complexity: O( 1 )
#
# The overhead is the event variable, which is of O( 1 )