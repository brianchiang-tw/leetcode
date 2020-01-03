# Read from the file words.txt and output the word frequency list to stdout.
with open('words.txt', 'r') as f:

    line = f.readline()
    
    
    word_occ_dict = {}
    
    while line:
    
        tokens = list( line.split() )

        for t in tokens:
        
            word_occ_dict[t] = word_occ_dict.get(t, 0) + 1
            
        line = f.readline()


    for word in sorted(word_occ_dict, key=word_occ_dict.get, reverse = True ):
    
        print(f'{word} {word_occ_dict[word]}')