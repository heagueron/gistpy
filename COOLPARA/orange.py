# list.split(), looping with enumerate, range()

def countOrange(text):
    
    orangeMentions = 0
    
    words = text.split()

    # Find the instances of 'orange' or 'Orange'
    for index, word in enumerate(words):
        if word == 'orange' or word == 'Orange':

            if index < 3:
                minIndex = 0
            else:
                minIndex = index - 3

            if index > len(words) - 3:
                maxIndex = len(words) - 1
            else:
                maxIndex = index + 3

            # See if this orange is related to a fruit:
            for x in range(minIndex, maxIndex):
                if words[x] in ['eat', 'fruit', 'slice', 'peel', 'juice']:
                    orangeMentions += 1
                    break   # break the loop to avoid duplicate counting for a same instance of orange

    print('Orange as a fruit mentions: ', orangeMentions)                
