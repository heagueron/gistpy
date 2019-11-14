# BASIC EXAMPLE WITH argparse ( positional and optional arguments )

import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("paragraph", help="A quoted paragraph. Example: \"I live on planet earth\"")
parser.add_argument(
    "-l",
    "--longest", 
    help="show paragraph longest words list.",
    action="store_true")
args = parser.parse_args()

text = args.paragraph

  

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

    print (f"\nNumber of words:\t\t\t {len(words)}" )
    print (f"Number of words with rare letter:\t {counter_rare}")
    print (f"Number of words 8 letters or longer:\t {counter_8}" )
    if args.longest:
        print (f"\nLongest words:\t\t\t\t {longest_words}" )

    print("*****")

    if ( len(words) > 10 and (counter_rare/len(words)) >= 0.1 and (counter_8/len(words)) >= 0.1 ):
        return True
    return False

print( CoolPara(text) )