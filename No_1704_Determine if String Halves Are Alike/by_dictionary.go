/*


Description:

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.



Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.



Example 3:

Input: s = "MerryChristmas"
Output: false



Example 4:

Input: s = "AbCdEfGh"
Output: true
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.

*/


package No_1704

import (
	"strings"
)

func halvesAreAlike(s string) bool {

	// -----------------------------------------

	// compute and return the number of vowel letters in s
	var countVowels func(s string) int

	countVowels = func(s string) int {

		vowel_dict := map[rune]bool{
			'a': true,
			'e': true,
			'i': true,
			'o': true,
			'u': true,
		}

		count := 0
		for _, char := range s {
			if vowel_dict[char] {
				count += 1
			}
		}

		return count
	}

	// -----------------------------------------

	size := len(s)

	// It is guaranteed that s is of even length
	midpoint := size / 2

	// get substring of a as well as b
	a, b := s[:midpoint], s[midpoint:]

	// convert to lowercase letters
	a, b = strings.ToLower(a), strings.ToLower(b)

	return countVowels(a) == countVowels(b)

}




// n : the character length of s

//// Time Complexity: O( n )
//
// The overhead in time is the cost of string copy as well as vowel counting, which is of O( n )

//// Space Complexity: O( n )
//
// The overhead in space is the storage for substring, which is of O( n )

// run "go test -v" in console to run unittest