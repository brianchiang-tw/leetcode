
from threading import Semaphore, Barrier
from time import sleep

class H2O:
    def __init__(self):
        
        self._h2o       = Barrier(3)
        self._atom_h    = Semaphore(2)
        self._atom_o    = Semaphore(1)

        
        pass


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        self._atom_h.acquire()
    
        # use _h2o barrier to make we have 2 H and 1 O
        self._h2o.wait()
                
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        
        self._atom_h.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        

        self._atom_o.acquire()
        
        # use _h2o barrier to make we have 2 H and 1 O
        self._h2o.wait()
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        
        self._atom_o.release()


## Time Complexity : O ( 1 )
#
# The overhead is the semaphore and barrier with constant resource lock

## Space Complexity : O( 1 )
#
# The overhead is the variable for semaphore and barrier of constant size