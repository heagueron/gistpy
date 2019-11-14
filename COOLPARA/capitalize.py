def capTitle(line):
    
    # Convert the original line in a list of words
    words = line.split()

    # Create a copy of the list 
    new_line = words[:]

    # First word always capitalized
    new_line[0] = new_line[0].capitalize()

    for index, word in enumerate(words):
        # Here we compare with a list of 'special words'
        if word not in ['a', 'the', 'of']:
            new_line[index] = word.capitalize()

    # Rebuild and return the modified line        
    return ' '.join(new_line)