import sys

def MatchingWordCount(fileHandle, wordlist):

    # Open the file, read mode
    my_file = open(fileHandle)

    # Get the file rows via comprehension list
    rows = [ line.split(' ') for line in my_file.read().splitlines() ]
    my_file.close()

    # Loop through the list of words:
    for word in wordlist:
        count = 0
        for row in rows:
            if word in row:
                count += 1
        print(f"Number of ocurrencies of the word \"{word}\" is {count}")  

# Main program start
text_filename = sys.argv[1]
my_list = ['a', 'only','genial','life','please','number','state']
MatchingWordCount(text_filename, my_list)

