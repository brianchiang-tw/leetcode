package No_0509

func fib(n int) int {

	var getFib func(int) int

	memo := map[int]int{0: 0, 1: 1}

	getFib = func(n int) int {

		// base cases
		if value, exist := memo[n]; exist == true {
			return value
		}

		// general cases
		fibN := getFib(n-1) + getFib(n-2)
		memo[n] = fibN

		return fibN
	}

	return getFib(n)
}

// n : the value of input

//// Time Complexity: O( n )
//
// The overhead in time is the cost of recursion depth with memoization, which is of O( n )

//// Sapce Complexity: O( n )
//
// The overhead in space is the storage for dictionary, which is of O( n )

// run "go test -v" in consonle to run unittest
