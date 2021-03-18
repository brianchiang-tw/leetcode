package main

func max(x, y int) int {

	if x > y {
		return x
	} else {
		return y
	}

}

func wiggleMaxLength(nums []int) int {

	n := len(nums)

	// length of wiggle sequence, ending in positive differnce, negative difference
	positive, negative := 1, 1

	// scan from second number to last number
	for i := 1; i < n; i++ {

		if nums[i] > nums[i-1] {

			// difference is positive, concatenated with negative prefix wiggle subsquence
			positive = negative + 1

		} else if nums[i] < nums[i-1] {

			// differnce is negative, concatenated with positive prefix wiggle subsequence
			negative = positive + 1
		}
	}

	// compute the longest length of wiggle sequene
	return max(positive, negative)
}


// n : the length of input nums

//// Time Complexity: O( n )
//
// The overhead in time is the cost of iteration, which is of O( n )

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )

// type "go test -v" in console to run unittest