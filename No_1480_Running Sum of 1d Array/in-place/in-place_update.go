package main

import (

)



func runningSum(nums []int) []int {
    
    prefixSum := nums
    
    for idx, _ := range nums{
        
        if idx == 0 {
			// first item
            continue
        }else {
			// others
            prefixSum[idx] = prefixSum[idx-1] + prefixSum[idx]
        }
    }
    
    return prefixSum
}


// n : the length of input list, nums

//// Time Complexity: O( n )
//
// The overhead in time is the cost of iteration, which is of O( n ).

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage for loop index, which is of O( 1 ).

// Note:
// type "go test -v" in console to launch local testbench

