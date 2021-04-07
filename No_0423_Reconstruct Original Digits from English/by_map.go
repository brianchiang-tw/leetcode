package No_0423

import (
	"strings"
	"strconv"
)

func originalDigits(s string) string {

	//// dictionary of input s
	// key: ascii character
	// value: occurrence of ascii character
	charOccDict := make(map[rune]int)

	for _, char := range s {
		charOccDict[char] += 1
	}

	//// dictionary
	// key: digit
	// value: occurrence of digit
	digitOccDict := make(map[int]int)

	// rebuild digit-occurrence mapping from input s and its char-occurrence mapping
	mapping_rebuild(&digitOccDict, &charOccDict)

	// rebuild digit string in ascending order
	outputString := ""

	for digit := 0; digit <= 9; digit++ {

		occurrence := digitOccDict[digit]
		outputString += strings.Repeat(strconv.Itoa(digit), occurrence)
	}

	return outputString
}

func mapping_rebuild(digitMap *map[int]int, letterMap *map[rune]int) {
	// Rebuild the number and its occurrence from character frequency analysis

	// "z" only shows up in "zero"
	(*digitMap)[0] = (*letterMap)['z']

	// "w" only shows up in "two"
	(*digitMap)[2] = (*letterMap)['w']

	// "u" only shows up in "four"
	(*digitMap)[4] = (*letterMap)['u']

	// "x" only shows up in "six"
	(*digitMap)[6] = (*letterMap)['x']

	// "g" only shows up in "eight"
	(*digitMap)[8] = (*letterMap)['g']

	// "o" only shows up in "zero", "one", "two", "four"
	(*digitMap)[1] = (*letterMap)['o'] - (*digitMap)[0] - (*digitMap)[2] - (*digitMap)[4]

	// "h" only shows up in "three", "eight"
	(*digitMap)[3] = (*letterMap)['h'] - (*digitMap)[8]

	// "f" only shows up in "four", "five"
	(*digitMap)[5] = (*letterMap)['f'] - (*digitMap)[4]

	// "s" only shows up in "six", "seven"
	(*digitMap)[7] = (*letterMap)['s'] - (*digitMap)[6]

	// "i" only shows up in "five", "six", "eight", "nine"
	(*digitMap)[9] = (*letterMap)['i'] - (*digitMap)[5] - (*digitMap)[6] - (*digitMap)[8]

}




// n : the character length of input string s

//// Time Complexity : O( n )
//
// The overhead in time is the cost of dictionary building, which is of O( n )

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage of dictionary, which is of O( 10 ) = O( 1 )

// type "go test -v" in console to run unittest