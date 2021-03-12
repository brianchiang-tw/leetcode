package main

import (

)

func peakIndexInMountainArray(arr []int) int {
    
    size := len(arr)
    
    // two pointers as search border guard, init to 0 and size-1
    left, right := 0, size-1
    
    // binary search core
    for left <= right{
        
        mid := left + (right - left) / 2

        if arr[mid-1] < arr[mid] && arr[mid] > arr[mid+1]{

            // hit directly get peak
            return mid

        }else if arr[mid-1] < arr[mid] && arr[mid] < arr[mid+1]{
            
            // current direction is uphill, so peak is on the right hand side
            left = mid
            
        }else{
            
            // current direction is downhill, so peak is on the left hand side
            right = mid
        }

    }
    
    return -1
}



// n : the length of mountain array

//// Time Complexity: O( log n )
//
// The overhead in time is the cost of binary search of a list of n, which is of O( n )

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage for loop index and binary search variable, which is of O( 1 )


// type "go test -v" in console to launch unittest