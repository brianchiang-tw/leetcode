/*

Description:

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.



Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.

*/

package No_0775

func isIdealPermutation(A []int) bool {

	globalInversion, localInversion := 0, 0

	size := len(A)

	for curIdx, curNum := range A {

		// for global inversion
		if curNum > curIdx {

			// current number is too big, update with the count with mismatch on smaller elements
			globalInversion += (curNum - curIdx)

		} else if curNum < curIdx {

			// current number is too small, update with the count with mismatch on larger elements
			globalInversion += (curIdx - curNum - 1)

		}

		// for local inversion
		if (curIdx < (size - 1)) && (A[curIdx] > A[curIdx+1]) {

			// current number is out-of-order, update with current mismatch pair
			localInversion += 1
		}

	}

	return globalInversion == localInversion
}

// n : the length of input list A

//// Time Complexity: O( n )
//
// The overhead in time is the cost of for-loop iteration, which is of O( n )

//// Space Complexity: O( 1 )
// The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )
