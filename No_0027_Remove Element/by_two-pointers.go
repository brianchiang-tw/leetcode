package main

func removeElement(nums []int, val int) int {

	size := len(nums)

	// two-pointers
	// otherIdx: index for other elements
	// targetIdx: index for target elements with val

	otherIdx, targetIdx := 0, size-1

	for otherIdx <= targetIdx {

		if nums[otherIdx] == val {

			// swap target elements to the tail side
			nums[otherIdx], nums[targetIdx] = nums[targetIdx], nums[otherIdx]

			targetIdx -= 1
		} else {

			// increase the index when we meet others
			otherIdx += 1
		}

	}

	// length of others is the answer
	return otherIdx

}

// n : the length of input nums

//// Time Complexity: O( n )
//
// The overhead in time is the cost of iteration, which is of O( n )

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage for two-pointers, which is of O( 1 )

// type "go test -v" in console to run unittest
