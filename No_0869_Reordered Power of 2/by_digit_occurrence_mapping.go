package main

import(
	"math"
)



func reorderedPowerOf2(N int) bool {
 
    var makeSignature func(n int) int
    
    makeSignature = func(n int) int {
        
        if n == 0{
            // base case
            return 0
        }
        
        // general case
        leading, remaining := n / 10, n % 10
        return makeSignature( leading ) + int( math.Pow(10, float64(remaining) ) )
        
    }
    
    // -----------------------------------------------------
    
    signatureN := makeSignature( N )
    
    // check each possible power of 2
    for i := 0 ; i < 32 ; i++ {
        
        if makeSignature( 1 << i ) == signatureN{
            
            // Accept if at least one power of 2's signature is the smae with N's
            return true
        }
        
    }
    
    // Reject otherwise
    return false
}


//// N : the input value

//// Time Complexity: O( log N )
//
// The overhead in time is the cost of recursion call stack, which is of O( log N )

//// Space Complexity: O( log N )
// 
// The overhead in space is the storage for recrsion call stack, which is of O( log N )

