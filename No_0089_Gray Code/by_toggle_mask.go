package main

import (

)


func grayCode(n int) []int{

	// total 2^n codes for bit length n
	code_count := 1 << n
	
	// slice to store gray codes
	gray_codes := make([]int, code_count)

	for i:=0; i<code_count; i+=1{
		toggle_mask := ( i >> 1 )

		gray_codes[ i ] = i ^ toggle_mask
	}

	return gray_codes
}
//End of function grayCode




// n : the value of input n

//// Time Complexity: O( n )
//
// The overhead in time is the cost of list comprehension, which is of O( n )

//// Space Complexity: O( n )
//
// The overhead in space is the storage for output list, which is of O( n )

// type "run test -v" in console to run uniitest