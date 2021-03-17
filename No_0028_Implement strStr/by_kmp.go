package main

func strStr(haystack string, needle string) int {

	var nextTable func(string) []int

	nextTable = func(pattern string) []int {

		sizePattern := len(pattern)

		// optimal rollback table
		next_arr := make([]int, sizePattern)

		next_arr[0] = -1

		i, j := 0, -1

		for i < (sizePattern - 1) {

			if (j == -1) || (pattern[i] == pattern[j]) {

				// first character, or common prefix exist

				i, j = i+1, j+1
				next_arr[i] = j
			} else {

				// not match, roll back
				j = next_arr[j]
			}
		}

		return next_arr

	}
	//End of inner function nextTable

	// Implement KMP algorithm

	if needle == "" {

		// Return 0 for empty string as pattern
		return 0
	}

	// compute optimal rollback table
	next_arr := nextTable(needle)

	i, j := 0, 0

	sizeSrc, sizePattern := len(haystack), len(needle)

	// keep comparing character till the end of string
	for (i < sizeSrc) && (j < sizePattern) {

		if (j == -1) || (haystack[i] == needle[j]) {

			// if reset or character match, go to compare next one
			i, j = i+1, j+1
		} else {

			// character mismatch, go back to optimal rollback index
			j = next_arr[j]

		}

	}

	if j == sizePattern {

		// Accept
		return i - sizePattern

	} else {

		// Reject
		return -1
	}

}

//End of function

// m : length of haystack
// n : length of needle

//// Time Complexity: O( m + n )
//
// The overhead in time is the cost of KMP algorithm, which is of O( m + n )

//// Space Complexity: O( n )
//
// The overhead in space is the storage for next_arr table, which is of O( n )

// type "go test -v" in console to run unittest
