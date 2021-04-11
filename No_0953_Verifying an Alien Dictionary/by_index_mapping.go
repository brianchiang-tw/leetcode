/*

Description:

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.



Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.



Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

*/

package No_0953

import (
    "unicode/utf8"
)

func isAlienSorted(words []string, order string) bool {

	// Step 1:
	// Build the index <-> character mapping relation based on givern alien order
    charIdxMapping := make(map[rune]int)
    
    for idx, char := range order{
        charIdxMapping[char] = idx
    }
    
    // -------------------------------------------
    
	// Step 2:
	// Convert each word to numerical mapping by dictionary
	
    var inorder func(s1, s2 string)bool
    
    inorder = func(s1, s2 string) bool{
        
        size1, size2 := len(s1), len(s2)
        
        for idx := 0 ; idx < size1 && idx < size2 ; idx++{
            
            rune1, _ := utf8.DecodeRuneInString(s1[idx:])
            rune2, _ := utf8.DecodeRuneInString(s2[idx:])
            order1, order2 := charIdxMapping[ rune1 ], charIdxMapping[ rune2 ]
            
            if  order1 > order2 {
                return false
                
            }else if order1 < order2 {
                return true
            }

        }
        
        return len(s1) <= len(s2)
    }
    
    
    // -------------------------------------------
    
	// Step 3:
	// Check each numerical mapping is sorted in ascending order
	
    for i:= 0; i < len(words)-1 ; i++{
        if !inorder(words[i], words[i+1]){
            return false
        }  
    }
    
    return true
}
