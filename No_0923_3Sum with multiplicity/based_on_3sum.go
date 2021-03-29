package No_0923

import (
	"math"
)

func threeSumMulti(arr []int, target int) int {

	//// dictionary
	// key: distinct number
	// value: occurrence of distinct number
	counts := genDictionary(arr)

	// total method count, and modulo constant
	result, constant := 0, int(math.Pow10(9))+7

	// find the method count where i + j + k = target
	// all numbers are bounded in interval [0, 100]

	for i := 0; i <= 100; i++ {

		if counts[i] == 0 {

			// number i doesn't show up in input array
			continue
		}

		j, k := i, 100

		// find j, k with two-pointers
		for j <= k {

			if (j + k) > (target - i) {

				// j + k is too large, try to make it smaller
				k -= 1

			} else if (j + k) < (target - i) {

				// j + k is too small, try to make it larger
				j += 1

			} else {

				// update result with difference combination cases
				if (i == j) && (j == k) {

					// all repeated: (i, j, k) = (i, i, i)
					result += counts[i] * (counts[i] - 1) * (counts[i] - 2) / 6

				} else if i == j {

					// i, j repeated: (i, j, k) = (i, i, k)
					result += counts[i] * (counts[i] - 1) * (counts[k]) / 2

				} else if j == k {

					// j, k repeated: (i, j, k) = (i, j, j)
					result += counts[i] * (counts[j]) * (counts[j] - 1) / 2

				} else {

					// all distinct: (i, j, k)
					result += counts[i] * counts[j] * counts[k]

				}

				// update two-pointers for j, k
				j, k = j+1, k-1
			}

		}
		//end of j <= k loop

	}
	//end of i loop

	return result % constant
}

func genDictionary(arr []int) (number_occ_dict map[int]int) {

	number_occ_dict = make(map[int]int, 101)

	for _, number := range arr {
		number_occ_dict[number] += 1
	}
	return
}

//// n : the length of inpu array

//// Time Compleity: O( n )
//
// The overhead in time is the cost of nested loop with O( n ) * O( 100 ) = O( n )

//// Space Complexity: O( n )
//
// The overhead in space is the storage for dictionary, which is of O( n )

// run "go test -v" in console to run unittest
