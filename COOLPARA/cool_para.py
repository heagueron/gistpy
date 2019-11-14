# BASIC EXAMPLE WITH AssertionError CHECK.

import sys

try:
    text = sys.argv[1]
except IndexError:
    text = 'a b c'

# EXCEPTIONS
# 1.Raise an exception directly if got less than 3 words. The program will come to halt and will not continue.
# if len(text.split()) < 3:
#     raise Exception("Input line must contain at least 3 words.")

# 2. AssertionError. The program will come to halt and will not continue.
assert (len(text.split()) >= 3), "Input line must contain at least 3 words."

#class ShortLine(Exception):   

def CoolPara(text):

    words = text.split()
    counter_rare = 0
    counter_8 = 0
    max_word_length = 0

    for word in words:        
        if('j' in word or 'x' in word or 'q' in word or 'z' in word):
            counter_rare += 1
        if len(word) >= 8:
            counter_8 += 1
        if len(word) >= max_word_length:
            max_word_length = len(word)
    
    longest_words = [n for n in words if len(n)==max_word_length]

    print (f"Number of words: {len(words)}" )
    print (f"Number of words with rare letter: {counter_rare}")
    print (f"Number of words 8 letters or longer: {counter_8}" )
    print (f"\nLongest words: {longest_words}" )

    print("*****")

    if ( len(words) > 10 and (counter_rare/len(words)) >= 0.1 and (counter_8/len(words)) >= 0.1 ):
        return True
    return False

# print( CoolPara(text) )

def xmul(a,b,c):
    return ( a * b ) + c
