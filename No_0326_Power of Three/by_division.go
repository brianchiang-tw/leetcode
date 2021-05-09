package No_0326

func isPowerOfThree(n int) bool {

	for n > 1 {

		if n % 3 != 0{

			// Early rejection to those number which is not multiple of 3
			return false
		}else{

			// keep dividing 3 if n is multiple of 3
			n /= 3
		}

	}

	return n == 1
}


// n : the value in of input n

//// Time Complexity: O( log n )
//
// The overhead in time is the cost of iteration of division, which is of O( log n )

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage of loop index and temporary variable, which is of O( 1 )
