package main

func peakIndexInMountainArray(arr []int) int {

	var binSearch func(arr []int, left int, right int) int

	binSearch = func(arr []int, left int, right int) int {

		if left == right {

			// base case
			return left
		}

		// binary search core
		mid := left + (right-left)/2

		if arr[mid-1] < arr[mid] && arr[mid] > arr[mid+1] {

			// hit directly get peak
			return mid

		} else if arr[mid-1] < arr[mid] && arr[mid] < arr[mid+1] {

			// current direction is uphill, so peak is on the right hand side
			return binSearch(arr, mid, right)

		} else {

			// current direction is downhill, so peak is on the left hand side
			return binSearch(arr, left, mid)
		}

	}

	size := len(arr)
	return binSearch(arr, 0, size-1)

}

// n : the length of mountain array

//// Time Complexity: O( log n )
//
// The overhead in time is the cost of binary search of a list of n, which is of O( n )

//// Space Complexity: O( log n )
//
// The overhead in space is the storage for recursion call stack, which is of O( log n )

// type "go test -v" in console to launch unittest
