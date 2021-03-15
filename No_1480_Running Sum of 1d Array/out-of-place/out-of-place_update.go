package main

import (
    
)



func runningSum(nums []int) []int {
    
    prefixSum := make([]int, 0)
    
    for idx, number := range nums{
        
        if idx == 0 {
            prefixSum = append(prefixSum, number)
        }else {
            prefixSum = append(prefixSum, number + prefixSum[len(prefixSum)-1])
        }
    }
    
    return prefixSum
}


// n : the length of input list, nums

//// Time Complexity: O( n )
//
// The overhead in time is the cost of iteration, which is of O( n ).

//// Space Complexity: O( n )
//
// The overhead in space is the storage for prefixSum, which is of O( n ).

// Note:
// type "go test -v" in console to launch local testbench

