package No_0916

/*
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order.



Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]



Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]



Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]



Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]



Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]


Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].

*/

func wordSubsets(A []string, B []string) []string {

	//// dictionary
	// key: distinct character
	// value: max occurence of distinct character among words in B
	charOccDict := genDict("")

	// compute maximum occrrence of distinct character in B
	for _, str := range B {

		curOccDict := genDict(str)

		pickMaxOccurrence(curOccDict, charOccDict)
	}

	universalWords := make([]string, 0)

	// scan each word in A
	for _, src := range A {

		srcOccDict := genDict(src)

		// current word has enough occurrence on every distinct character to cover B
		if contains(srcOccDict, charOccDict) {

			universalWords = append(universalWords, src)
		}
	}

	return universalWords
}

// generate character<->occurrence mapping from string
func genDict(s string) *map[rune]int {

	charOccDict := make(map[rune]int)

	for _, char := range s {

		charOccDict[char] += 1

	}

	return &charOccDict
}

// max function for two integers
func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// pick maximum occurrence between src, and dst.
// save maximum occurrence to dst
func pickMaxOccurrence(src *map[rune]int, dst *map[rune]int) {

	for letter := 'a'; letter <= 'z'; letter++ {
		(*dst)[letter] = max((*dst)[letter], (*src)[letter])
	}
}

// check whether src dictionary can cover target dictionary
func contains(src *map[rune]int, target *map[rune]int) bool {

	for letter := 'a'; letter <= 'z'; letter++ {
		if (*src)[letter] < (*target)[letter] {
			return false
		}
	}

	return true
}

// m : total characters from list A
// n : total characters from list B

//// Time Complexity: O( m + n )
//
// The overhead in time is the cost of dictionary operation, which is of O( A + B )

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage of dictioanry, which is of O( 26 ) = O( 1 )

// run "go test -v" in console to run unittest
